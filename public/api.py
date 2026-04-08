import json

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
connected = False
db = None

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    db = client["eslsca-course"]
    connected = True
    print("Connected to MongoDB")
except ConnectionFailure:
    print("MongoDB connection failed")

# if connected:
#     print(f"list_collection_names : {db.list_collection_names()}")

#     collection = db["students"]
#     documents = collection.find()
#     for doc in documents:
#         print(doc)


from flask import Flask, jsonify
app = Flask(__name__)

# API Routes
@app.route("/bonjour", methods=["GET"])
def say_hello():
    return jsonify({"status": "success", "result": "bonjour"})


@app.route("/students", methods=["GET"])
def get_students():
    try:
        collection = db["students"]
        documents = list(collection.find())
        return jsonify({"status": "succeess", "reason": "", "result": json.dumps(documents, default=str)})
    except Exception as e:
        return jsonify({"status": "failed", "reason": str(e), "result": []})

# Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
