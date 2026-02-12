import os
from google import genai
 
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
 
def gemini_llm(content):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents = content
    )
    return response.text
 