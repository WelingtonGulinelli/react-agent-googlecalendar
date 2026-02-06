import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.chat_models import BaseChatModel

load_dotenv()

def load_llm() -> BaseChatModel:
    return ChatOllama(
    model=os.getenv("OLLAMA_MODEL_NAME"),
    base_url=os.getenv("OLLAMA_BASE_URL"), 
    temperature=0
)