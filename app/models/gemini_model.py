from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key = os.getenv("GEMINI_API_KEY")

)