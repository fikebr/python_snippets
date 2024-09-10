import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access variables using os.getenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
