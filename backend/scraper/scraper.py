from pathlib import Path
import os
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv


def _ensure_env_loaded():
    # Load .env first if present
    load_dotenv()  # default .env
    # Also try backend/.env.dev as a non-overriding fallback
    dev_env = Path(__file__).resolve().parents[1] / ".env.dev"
    if dev_env.exists():
        load_dotenv(dev_env, override=False)


def create_vector_db(urls):
    _ensure_env_loaded()

    # Initialize embeddings only when needed (after env is loaded)
    embedding = OpenAIEmbeddings()

    loader = SeleniumURLLoader(urls)
    documents = loader.load()

    txt_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = txt_splitter.split_documents(documents)

    database = FAISS.from_documents(docs, embedding)
    return database


    
