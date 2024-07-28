# Import necessary libraries
""" 
Simple application to perform basic Create, read, update, and delete (CRUD) operations using Python's and MongoDB as database.
"""

from pprint import pprint
import pymongo
from bson.dbref import DBRef

# Make the connection
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5")
db = client["db_data"]
patient_collection = db["patient"]

# Insert data
patient_records = [
    {
    "Name": "Margarett Collins",
    "Age": 65,
    "Sex": "F",
    "Weight": 182.01,
    "Height": 190,
    "Blood pressure": [{"sys": 133}, {"dia": 74}],
    "Heart rate": 74,
    "Blood Type": "A+",
    "allergies": ["Pollen", "Penicillin"],
    "Address": [
        {
        "Address_1": "1 South Main Street",
        "Address_2": "Suite 200",
        "City": "Dayton",
        "State": "Ohio",
        "Zipcode": "45402",
        }
        ]
    },
    
    {
    "Name": "Olie Sanders",
    "Age": 46,
    "Sex": "M",
    "Weight": 148.46,
    "Height": 188,
    "Blood pressure": [{"sys": 120}, {"dia": 70}],
    "Heart rate": 68,
    "Blood Type": "B+",
    "allergies": ["Pollen", "Penicillin"],
    "Address": [
        {
        "Address_1": "450 Inah Ave",
        "Address_2": "Apt 11",
        "City": "Columbus",
        "State": "Ohio",
        "Zipcode": "43228",
        }
    ]
    },
    
    {
    "Name": "Bernadette Joyce",
    "Age": 13,
    "Sex": "F",
    "Weight": 105,
    "Height": 63,
    "Blood pressure": [{"sys": 121}, {"dia": 72}],
    "Heart rate": 67,
    "Blood Type": "AB+",
    "allergies": ["Food allergies", "Penicillin"],
    "Address": [
        {
        "Address_1": "1401 Missouri Street",
        "Address_2": "",
        "City": "Delaware",
        "State": "Ohio",
        "Zipcode": "43105", 
        }
    ],
    "phone_numbers": [
    {
        "number": "1-541-754-3010",
        "type": "Mobile"
    }] 
    },

    {
    "Name": "Michel Barry",
    "Age": 17,
    "Sex": "F",
    "Weight": 62.69,
    "Height": 157,
    "Blood pressure": [{"sys": 146}, {"dia": 80}],
    "Heart rate": 81,
    "Blood Type": "O+",
    "allergies": ["Hayfever", "Asthma"],
    "Address": [
    {
    "Address_1": "1171 Gabrielle Elaine Dr",
    "Address_2": "suite 105",
    "City": "Columbus",
    "State": "Ohio",
    "Zipcode": "43228",
    }
    ],
    "Prescribed medications": [
    DBRef("diagnosis_data", "70a3e4e5g463205590d8790")
    ]
    },
    
    {
    "Name": "Bob Joyce",
    "Age": 25,
    "Sex": "M",
    "Weight": 105,
    "Height": 63,
    "Blood pressure": [{"sys": 110}, {"dia": 82}],
    "Heart rate": 77,
    "Heart rate": 81,
    "Blood Type": "O",
    "Address": [
        {
        "Address_1": "1600  Woodland Heights Ln",
        "Address_2": "",
        "City": "Lancaster",
        "State": "Ohio",
        "Zipcode": "43130", 
        }
    ]
    },   
]

patient_collection.insert_many(patient_records)

# Update documents
# patient_collection.update_one({"Name": "Margarett Collins"}, {"$set":{"Heart rate": 78}})
# Find all the documents with a Heart rate < 75 and Age > 30

# Filtering the Data
result = patient_collection.find({
 "$and" : [
     {
         "Heart rate": {"$lte": 75}
     },
     {
         "Age": {"$gt": 30}
     }
   ]
})
for rate in result:
    pprint(rate)
    