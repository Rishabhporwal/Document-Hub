import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentHubException

from models.models import *
from prompt.prompt_library import *

from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentAnalyzer:
    """
        Analyze documents using pre-trained models
        Automatically logs all actions and supports session-based organization
    """

    def __init__(self):
        self.log = CustomLogger().get_logger(__name__)

        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()

            # Prepare Models
            self.parser = JsonOutputParser(pydantic_object=MetaData)
            self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm = self.llm)

            self.prompt = prompt

            self.log.info("Document Analyzer initialized successfully")

        except Exception as e:
            self.log.error(f"Error while initializing DocumentAnalyzer: {e}")
            raise DocumentHubException("Error in documentAnalyzer initialization", sys)

    def analyze_document(self, document_text: str) -> dict:
        try:
            chain = self.prompt | self.llm | self.fixing_parser

            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "document_text": document_text
            })

            self.log.info("metadata extraction successful", keys=list(response.keys()))
            return response
        except Exception as e:
            self.log.error(f"Error while initializing DocumentAnalyzer: {e}")
            raise DocumentHubException("Error in documentAnalyzer initialization", sys)
    
