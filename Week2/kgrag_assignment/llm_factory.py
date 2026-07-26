from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from settings import Settings

load_dotenv()

def get_llm() -> ChatOpenAI:
    """
    Return the configured ChatOpenAI model.
    """

    return ChatOpenAI(
        model=Settings.OPENAI_MODEL,
        temperature=Settings.TEMPERATURE
    )