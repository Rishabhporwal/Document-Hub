import sys
import uuid
from pathlib import Path
import fitz
from datetime import datetime, timezone

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentHubException

class DocumentIngestion:
    def __init__(self, base_dir: str= "data\\document_compare", session_id = None):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        self.session_path = self.base_dir / self.session_id
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_uploaded_files(self, reference_file, actual_file):
        """
        Saves uploaded files to a specific directory.
        """
        try:
            ref_path = self.base_dir/ reference_file.name
            act_path = self.base_dir/ actual_file.name

            if not reference_file.name.endswith(".pdf") or not actual_file.name.endswith(".pdf"):
                raise ValueError("Only pdfs are allowed")
            
            with open(ref_path, 'wb') as f:
                f.write(reference_file.getbuffer())

            with open(act_path, 'wb') as f:
                f.write(actual_file.getbuffer())

            self.log.info("Files Saved", reference=str(ref_path), actual = str(act_path))

            return ref_path, act_path

        except Exception as e:
            self.log.error(f"Error saving pdf: {e}")
            raise DocumentHubException("Error while saving uploaded the pdf", sys)

    def read_pdf(self, pdf_path: Path) -> str:
        """
        Reads a PDF file and extracts text from each page.
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError(f"PDF is encrypted: {pdf_path}")

                all_text = []
                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    text = page.get_text() # type: ignore

                    if text.strip():
                        all_text.append(f"\n ---Page {page_num+1} --- \n {text}")
                self.log.info("PDF Read successfully", file=str(pdf_path), pages=len(all_text))
                
                return '\n'.join(all_text) 

        except Exception as e:
            self.log.error(f"Error reading pdf: {e}")
            raise DocumentHubException("Error while reading the pdf", sys)
        

    def combine_documents(self):
        try:
            """
            Combine content of all PDFs in session folder into a single string.
            """
            doc_parts = []

            for filename in sorted(self.base_dir.iterdir()):
                if filename.is_file() and filename.suffix.lower() == ".pdf":
                    content = self.read_pdf(filename)
                    doc_parts.append(f"Document: {filename.name}\n{content}")

            combined_text = "\n\n".join(doc_parts)
            self.log.info("Documents combined", count=len(doc_parts), session=self.session_id)
            return combined_text

        except Exception as e:
            self.log.error(f"Error combining documents: {e}")
            raise DocumentHubException("An error occurred while combining documents.", sys)


    def clean_old_sessions(self, keep_latest: int = 3):
        """
        Optional method to delete older session folders, keeping only the latest N.
        """
        try:
            session_folders = sorted(
                [f for f in self.base_dir.iterdir() if f.is_dir()],
                reverse=True
            )
            for folder in session_folders[keep_latest:]:
                for file in folder.iterdir():
                    file.unlink()
                folder.rmdir()
                self.log.info("Old session folder deleted", path=str(folder))

        except Exception as e:
            self.log.error("Error cleaning old sessions", error=str(e))
            raise DocumentHubException("Error cleaning old sessions", sys)