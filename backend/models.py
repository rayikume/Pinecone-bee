from langchain_openai import ChatOpenAI
from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from scraper.scraper import create_vector_db
from flask import Blueprint, jsonify, request
import gc
import replicate

models_bp = Blueprint(__name__, "models")

load_dotenv()

urls = [
            'https://u.ae/en/information-and-services#/',
            'https://u.ae/en/information-and-services/top-government-services',
            'https://u.ae/en/information-and-services/visa-and-emirates-id',
            'https://u.ae/en/information-and-services/jobs',
            'https://u.ae/en/information-and-services/education',
            'https://u.ae/en/information-and-services/business',
            'https://u.ae/en/information-and-services/moving-to-the-uae',
            'https://u.ae/en/information-and-services/justice-safety-and-the-law',
            'https://u.ae/en/information-and-services/visiting-and-exploring-the-uae',
            'https://u.ae/en/information-and-services/transportation',
            'https://u.ae/en/information-and-services/finance-and-investment',
            'https://u.ae/en/information-and-services/environment-and-energy',
            'https://u.ae/en/information-and-services/housing',
            'https://u.ae/en/information-and-services/health-and-fitness',
            'https://u.ae/en/information-and-services/passports-and-traveling',
            'https://u.ae/en/information-and-services/public-holidays-and-religious-affairs',
            'https://u.ae/en/information-and-services/infrastructure',
            'https://u.ae/en/information-and-services/social-affairs',
            'https://u.ae/en/information-and-services/charity-and-humanitarian-work',
            'https://u.ae/en/information-and-services/g2g-services',
        ]
    
vector_database = create_vector_db(urls)

def get_response_ChatGPT3(database, query, tk=8):
    docs = database.similarity_search(query, tk=tk)
    docs_merge = " ".join([page.page_content for page in docs])

    llm = ChatOpenAI(model="gpt-3.5-turbo")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
            You are a AI Assistant that help answering the user any question regarding United Arab Emirates laws and culture, that include any questions about: 
            Services of each ministry, Visa laws and regulations, jobs, education, business, moving to the uae, justice safety and law, visiting and exploring the uae,
            transportation, finance and investment, environment and energy, housing, health and fitness, passport and traveling guidlines, public hoildays, infrastructure,
            social affairs, charity and G2G.

            Answer the following question: {question}
            By ONLY using this database consist of scrapped information from the offical UAE government website: {docs}

            If you feel like you don't have enough information to answer the question, just say I don't know.
            If the question provided not in any way related to United Arab Emirates, simply say that the question is not related to the subject.

            Your answers should be detailed.
        """,
    )

    chain = prompt | llm

    response = chain.invoke({"question": query, "docs": docs_merge})
    response_content = response.content
    response_formatted = response_content.replace("\n", " ")

    return response_formatted

def get_response_ChatGPT4(database, query, tk=8):
    docs = database.similarity_search(query, tk=tk)
    docs_merge = " ".join([page.page_content for page in docs])

    llm = ChatOpenAI(model="gpt-4")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template= """
            You are a AI Assistant that help answering the user any question regarding United Arab Emirates laws and culture, that include any questions about: 
            Services of each ministry, Visa laws and regulations, jobs, education, business, moving to the uae, justice safety and law, visiting and exploring the uae,
            transportation, finance and investment, environment and energy, housing, health and fitness, passport and traveling guidlines, public hoildays, infrastructure,
            social affairs, charity and G2G.

            Answer the following question: {question}
            By ONLY using this database consist of scrapped information from the offical UAE government website: {docs}

            If you feel like you don't have enough information to answer the question, just say I don't know.
            If the question provided not in any way related to United Arab Emirates, simply say that the question is not related to the subject.

            Your answers should be detailed.
        """,
    )

    chain = prompt | llm

    response = chain.invoke({"question": query, "docs": docs_merge})
    response_content = response.content
    response_formatted = response_content.replace("\n", " ")

    return response_formatted

def get_response_llama(database, query):
    docs = database.similarity_search(query)
    tmp = f"You are a AI Assistant that help answering the user any question regarding United Arab Emirates laws and culture, that include any questions about: Services of each ministry, Visa laws and regulations, jobs, education, business, moving to the uae, justice safety and law, visiting and exploring the uae, transportation, finance and investment, environment and energy, housing, health and fitness, passport and traveling guidlines, public hoildays, infrastructure social affairs, charity and G2G. By ONLY using this database consist of scrapped information from the offical UAE government website: {docs} If you feel like you don't have enough information to answer the question, just say I don't know. If the question provided not in any way related to United Arab Emirates, simply say that the question is not related to the subject. Your answers should be detailed."

    input = {
        "top_p": 1,
        "prompt": query,
        "temperature": 0.5,
        "system_prompt": tmp,
        "max_new_tokens": 500
    }

    output = replicate.run(
        "meta/llama-2-70b-chat",
        input=input
    )

    return "".join(output)

stored_responses = {
    "ChatGPT3": "",
    "ChatGPT4": "",
    "llama": ""
}

@models_bp.route("/", methods=["POST", "GET", "OPTIONS"])
def models():
    global stored_responses
    
    if request.method == 'OPTIONS':
        response = jsonify({"status": "ok"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response, 200
    
    if request.method == "POST":
        data = request.get_json()
        inputValue = data['question']
        stored_responses["ChatGPT3"] = get_response_ChatGPT3(vector_database, inputValue)
        stored_responses["ChatGPT4"] = get_response_ChatGPT4(vector_database, inputValue)
        stored_responses["llama"] = get_response_llama(vector_database, inputValue)
        gc.collect()
        
        response = jsonify(stored_responses)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200
    
    if request.method == "GET": 
        response = jsonify(stored_responses)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    return jsonify({"error": "Invalid request method"}), 405