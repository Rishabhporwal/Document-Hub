import uuid
import sys
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentHubException

from utils.model_loader import ModelLoader

class SingleDocIngestor:
    def __init__(self):
        try:
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Failed to initialize SingleDocIngestor", error=str(e))
            raise DocumentHubException("Initialization error in SingleDocIngestor", sys)
        

    def ingest_file(self):
        try:
            pass
        except Exception as e:
            self.log.error("Document ingestion failed", error=str(e))
            raise DocumentHubException("Error during file ingestion", sys)

    def create_retriever(self):
        try:
            pass
        except Exception as e:
            self.log.error("Retriever creation failed", error=str(e))
            raise DocumentHubException("Error creating FAISS retriever", sys)