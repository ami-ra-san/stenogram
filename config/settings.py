import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN_BOT")

if BOT_TOKEN is None:
    raise ValueError(
        "TELEGRAM_TOKEN_BOT is not set. "
        "Did you create a .env file with that key?"
    )