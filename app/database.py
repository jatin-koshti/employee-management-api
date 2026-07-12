from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URI:
    raise Exception("MONGODB_URI environment variable not found")

if not DATABASE_NAME:
    raise Exception("DATABASE_NAME environment variable not found")

client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]

employees = db["employees"]

print("✅ MongoDB Connected")