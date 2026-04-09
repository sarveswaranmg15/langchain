from app.models.groq_model import model as groq_model
from app.models.gemini_model import model as gemini_model
from app.utils.constants import SYSTEM_PROMPT
import json

def invoke_model(query: str):
    response = groq_model.invoke(
    [
        {
            "role":"system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content":f"""Question: {query}"""
        }

    ]
    )
    return json.loads(response.content)