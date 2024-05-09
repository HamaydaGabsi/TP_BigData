import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['football']  # Replace 'your_database_name' with your desired database name
collection = db['goals_per_season']  # Replace 'your_collection_name' with your desired collection name

# Read data from CSV file
df = pd.read_csv('data.csv')

# Assuming the first row contains column names
# Convert the DataFrame to a list of dictionaries
data = df.to_dict('records')

# Insert the data into MongoDB
collection.insert_many(data)

print("Data successfully loaded into MongoDB.")
