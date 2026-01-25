from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key=os.getenv("Study_API_Key"))

def generate_questions(text):
    prompt = f"""
    Read the following PDF content and make:
    - 5 MCQs with 4 options each  
    
    You must return the output in clean, beautiful Markdown.

   Example format:

    ###MCQs
  1. **Question?**
   - A)
   - B)
   - C)
   - D)

    Content:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content