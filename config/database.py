from pymongo import MongoClient

client = MongoClient("Your-Database-Connection-String")

db = client.social_app_db

collection_name = db["social_app_collection"]