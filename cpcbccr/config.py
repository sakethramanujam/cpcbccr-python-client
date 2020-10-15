import os

DEFAULT_API_URL = "https://love-the-air.herokuapp.com/api"
API_URL = os.getenv("API_URL") or DEFAULT_API_URL