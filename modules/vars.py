import os

API_ID    = os.environ.get("API_ID", "20945078")
API_HASH  = os.environ.get("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
