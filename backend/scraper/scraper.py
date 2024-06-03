from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import time
import re

load_dotenv()

embedding = OpenAIEmbeddings()

def create_vector_db(urls):
    loader = SeleniumURLLoader(urls)
    documents = loader.load()

    txt_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = txt_splitter.split_documents(documents)

    database = FAISS.from_documents(docs, embedding)
    return database


    