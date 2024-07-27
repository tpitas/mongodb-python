from Extract import * # Import our custom built extract module

class Load:
    def from_csv(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
    
    def to_mongodb(self, host, port, username, password, db, collection, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not collection:
            raise Exception("Input a valid collection name.")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port, username = username, password = password)
        mongo_database = client[db]
        mongo_collection = mongo_database[collection]
        mongo_collection.insert_many(dataset)

# Inserting data
lo = Load()
# MongoDB Connection strings
lo.to_mongodb(host = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5", 
              port = 27017, username = "barry", password = "Passw0rd", db = "cogsley", collection = "cogsley_sales", dataset = dataset) 

# After running the script, we can verify that the data was added to the collection using a MongoDB client command:
# mongosh
# use cogsley
# db.cogsley_sales.find()
