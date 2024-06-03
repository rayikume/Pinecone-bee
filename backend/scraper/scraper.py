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

# def main():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     service = Service(executable_path="chromedriver.exe")
#     driver = webdriver.Chrome(service=service)

#     try:
#         urls = [
#             'https://u.ae/en/information-and-services#/',
#             'https://u.ae/en/information-and-services/top-government-services',
#             'https://u.ae/en/information-and-services/visa-and-emirates-id',
#             'https://u.ae/en/information-and-services/jobs',
#             'https://u.ae/en/information-and-services/education',
#             'https://u.ae/en/information-and-services/business',
#             'https://u.ae/en/information-and-services/moving-to-the-uae',
#             'https://u.ae/en/information-and-services/justice-safety-and-the-law',
#             'https://u.ae/en/information-and-services/visiting-and-exploring-the-uae',
#             'https://u.ae/en/information-and-services/transportation',
#             'https://u.ae/en/information-and-services/finance-and-investment',
#             'https://u.ae/en/information-and-services/environment-and-energy',
#             'https://u.ae/en/information-and-services/housing',
#             'https://u.ae/en/information-and-services/health-and-fitness',
#             'https://u.ae/en/information-and-services/passports-and-traveling',
#             'https://u.ae/en/information-and-services/public-holidays-and-religious-affairs',
#             'https://u.ae/en/information-and-services/infrastructure',
#             'https://u.ae/en/information-and-services/social-affairs',
#             'https://u.ae/en/information-and-services/charity-and-humanitarian-work',
#             'https://u.ae/en/information-and-services/g2g-services',
#         ]

#         print(create_vector_db(urls))
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()


    