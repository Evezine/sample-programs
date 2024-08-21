import pymongo

# Establish the connection to MongoDB
mongocon = pymongo.MongoClient("mongodb://localhost:27017")

# Access the database named 'mydatabase'
mydb = mongocon["mydatabase"]

# Access the collection named 'customers' within 'mydatabase'
mycol = mydb["customers"]

# Document to be inserted
mydoc = {"name": "vish", "course": "Python", "Degree": "MCA"}

# # Insert the document into the collection
# insertmy = mycol.insert_one(mydoc)

# # Output the inserted document ID (optional)
# print("Document inserted with ID:", insertmy.inserted_id)
x= mycol.find_one()
print(x)