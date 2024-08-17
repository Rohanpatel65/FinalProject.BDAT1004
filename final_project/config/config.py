from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
FIREBASE_DATABASE_URL = os.getenv('FIREBASE_DATABASE_URL')