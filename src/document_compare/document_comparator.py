import sys
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentHubException

from models.models import *

from prompt.prompt_library import PROMPT_REGISTRY

from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparatorLLM:
    def __init__(self):
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__)
        self.model = ModelLoader()
        self.llm = self.model.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser(parser=self.parser, llm= self.llm)
        self.prompt = PROMPT_REGISTRY['document_comparison']
        self.chain = self.prompt | self.llm | self.parser | self.fixing_parser
        self.log.info("DocumentComparatorLLM is initialized with model and parser")

    def compare_document(self):
        """
        Compares two documents and returns a structured comparison.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in comparing documents: {e}")
            raise DocumentHubException("An error occured while comparing document.", sys)

    def _format_response(self):
        """
        Formats the response from the LLM into a structured format.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in formating response in dataframe", errors=str(e))
            raise DocumentHubException("Error formating response", sys)
