from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please add it to your .env file.")
