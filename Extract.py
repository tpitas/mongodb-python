# Import Libraries
import csv
import pymongo

class Extract:
    def from_csv(self, file_path, delimiter = ",", quotechar = ","):
        if not file_path:
            raise Exception("Please provide a valid file path")

        dataset = []
        with open(file_path) as file: 
            csv_file = csv.DictReader(file, delimiter = delimiter,quotechar = quotechar) 
            for row in csv_file:
                dataset.append(row)
        return dataset


ex = Extract()
dataset = ex.from_csv(file_path = '<------->/cogsley_sales.csv', delimiter = ',') # To be replaced by file path
print(dataset)