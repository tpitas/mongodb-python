# Import libraries
from pymongo import MongoClient
import pprint

# Establish a connection
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5", 27017)

# Access the database named webinars
db = client.webinars

# Access a collection named webinar
webinar = db.webinar

# Insert a single document
webinar1 = {
    "title": "Data Engineering with Scala and Spark",
    "author": "Eric Tome",
    "speakers": ["Eric Tome", "Rupam Bhattacharjee", "David Radford"],
    "url": "https://learning.oreilly.com/library/view/data-engineering-with/9781804612583/",
    "date": "06-10-2024 13:00:00 EDT",
    "duration": "180 minutes", 
}
result = webinar.insert_one(webinar1)
print(f"One webinar inserted: {result.inserted_id}")

# Insert four additional documents
webinar2 = {
    "title": "Databricks summit 2024 AI/Machine Learning",
    "author": "Adam Hewson",
    "speakers": ["Ajay Gollapalli", "Alberto Rizzoli", "Ali Dasdan"],
    "url": "https://www.databricks.com/dataaisummit/speakers?page=1&category=ai-machine-learning&industry=professional-services",
    "date": ["06-11-2024 13:00:00 EDT", "06-12-2024 13:00:00 EDT", "06-13-2024 13:00:00 EDT",],    
    "duration": "480 minutes", 
}

webinar3 = {
    "title": "Data Engineering in the Age of AI",
    "author": "Michael Armbrust",
    "speakers": ["Ori Zohar", "Matt Jones", "Vikas Ranjan", "Frank Munz", "Stephanie Rivera"],
    "url": "https://www.databricks.com/resources/webinar/data-engineering-age-ai",
    "date": "06-12-2024 13:00:00 EDT",
    "duration": "120 minutes", 
}

webinar4 = {
    "title": "Developing Data & AI Products",
    "author": "Sagar Paul",
    "speakers": ["Logan Clark"],
    "url": "https://www.datacamp.com/webinars/developing-data-and-ai-products",
    "date": "08-08-2024 13:00:00 EDT",
    "duration": "180 minutes", 
}

webinar5 = {
    "title": "How LLMs Work",
    "author": "Kate Harwood",
    "speakers": "",
    "url": "https://learning.oreilly.com/live-events/how-llms-work/0790145066962/0642572003267/",
    "date": "08-10-2024 13:00:00 EDT",
    "duration": "90 minutes", 
}

new_result = webinar.insert_many([webinar2, webinar3, webinar4, webinar5])
print(f"Four webinars have been inserted: {new_result.inserted_ids}")

# Retrieve all documents
for doc in webinar.find():
    pprint.pprint(doc)

# Retrieve a single document
jon_webinar = webinar.find_one({"author": "Adam Hewson"})
pprint.pprint(jon_webinar)

# Close the connection
with MongoClient() as client:
    db = client.webinars
    for doc in db.webinar.find():
        pprint.pprint(doc)
