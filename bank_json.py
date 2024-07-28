# Import necessary libraries
import json
from pymongo import MongoClient 
 
# Make the connection
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5") 
# Database 
# db = client["json_data"]
db = client["db_data"]

# Create a collection called bank_collection
bank_collection = db["banks"]

# Loading or Opening the json file
with open('/Users/thiernobarry/Desktop/Datasets/Oreilly_2024/JobReadyPython/data/bank_transactions.json') as file:
    file_data = json.load(file)
     
# Inserting the loaded data in the bank_collection
# If Json contains data more than one entry
# Insert_many documents is used or insert_one is used
if isinstance(file_data, list):
    bank_collection.insert_many(file_data)  
else:
    bank_collection.insert_one(file_data)
    
# Filtering the Data 
result = bank_collection.find({
 "$or" : [
     {
         "DEPOSIT AMT": {"$lte": 200000}
     },
     {
         "DATE": {"$gt": "01/01/2018"}
     }
   ]
})

list(map(print, result))