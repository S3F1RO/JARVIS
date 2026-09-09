import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
}

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

MISTRAL_BASE_URL = os.getenv(
    "MISTRAL_BASE_URL",
    "https://api.mistral.ai/v1",
)

MISTRAL_MODEL = os.getenv(
    "MISTRAL_MODEL",
    "mistral-medium-latest",
)