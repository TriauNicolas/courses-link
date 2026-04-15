from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
connected = False
db = None

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=20000)
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

from flask import Flask, jsonify, request
app = Flask(__name__)

# API Routes
@app.route("/bonjour", methods=["GET"])
def say_hello():
    return jsonify({
        "status": "success", 
        "result": "bonjour"
    })

@app.route("/students", methods=["GET"])
def get_students():
    try:
        collection = db["students"]
        documents = list(collection.find())
        for doc in documents:
            doc["_id"] = str(doc["_id"])

        return jsonify({
            "status": "succeess", 
            "reason": "", 
            "result": documents
        })
    except Exception as e:
        return jsonify({
            "status": "failed", 
            "reason": str(e), 
            "result": []
        })

@app.route("/student", methods=["POST"])
def add_student():
    try:
        collection = db["students"]
        document = request.get_json()
        document_to_insert = {
            "name": document.get("name", ""),
            "age": int(document.get("age", 0)),
            "gender": document.get("gender", "")
        }
        result = collection.insert_one(document_to_insert)

        return jsonify({
            "status": "succeess", 
            "reason": "", 
            "result": str(document_to_insert)
        })
    except Exception as e:
        return jsonify({
            "status": "failed", 
            "reason": str(e), 
            "result": []
        })

# Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
