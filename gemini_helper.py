import google.generativeai as genai  # Importing the library
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use correct model name
    response = model.generate_content(prompt)
    return response.text
