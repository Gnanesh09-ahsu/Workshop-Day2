import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def create_client():
    """Create a Gemini client using the API key from .env."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to your .env file."
        )

    return genai.Client(api_key=api_key)


def model_name():
    """Return the configured Gemini model."""
    return os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
