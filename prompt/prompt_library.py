from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
        You are a highly capable assistant trained to analyze and summerize documents.
        return the only json matching the exact schema below.

                                            
        {format_instructions}

        Analyze this document:
        {document_text}                                      
    """
)