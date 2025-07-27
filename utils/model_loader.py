import os
from dotenv import load_dotenv

from utils.config_loader import load_config

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentHubException

log = CustomLogger().get_logger(__file__)

class ModelLoader:
    def __init__(self):
        pass

    def _validate_env(self):
        pass

    def load_embeddings(self):
        pass

    def load_llm(self):
        pass
