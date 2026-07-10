from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client[os.getenv("DATABASE_NAME")]

employees = db["employees"]

print("✅ MongoDB Connected")