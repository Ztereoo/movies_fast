import os
from dotenv import load_dotenv
from typing import Literal

load_dotenv()

KEY = os.getenv("KEY", "default_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER", "default@gmail.com")
SMTP_PASS = os.getenv("SMTP_PASS", "default_password")

MODE: Literal['DEV', 'TEST', 'PROD'] = os.getenv("MODE", "DEV")
