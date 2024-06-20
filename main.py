import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

google_API = os.getenv("google_API")

genai.configure(api_key = google_API)
model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    query = input("Enter the input : ")
    reponse = model.generate_content(query)
    print(reponse.text)
