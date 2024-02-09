from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGODB")
client = MongoClient(uri)

db = client.Signify
collection = db["Signs"]