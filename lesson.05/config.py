import os
from dotenv import load_dotenv


load_dotenv()

TOKEN_TG = os.getenv("TOKEN_TELEGRAM")
TOKEN_WEATHER = os.getenv("TOKEN_OPENWEATHER")