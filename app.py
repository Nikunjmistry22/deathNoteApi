from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGODB_URI")
db_name=os.getenv("DB_NAME")
character_collection=os.getenv("CHARACTER_COLLECTION")
episode_collection=os.getenv("EPISODE_COLLECTION")
client = MongoClient(uri)
db = client.anime
app = Flask(__name__, template_folder='template',static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')
def get_total_documents_count(collection_name):
    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        total_count = collection.count_documents({})
        return total_count
    else:
        return 0


@app.route('/characters', methods=['GET'])
def get_collection_documents(collection_name=character_collection):
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        total_count = get_total_documents_count(collection_name)
        skip = (page - 1) * limit
        documents = []
        for doc in collection.find().skip(skip).limit(limit):
            doc['_id'] = str(doc['_id'])
            documents.append(doc)

        return jsonify({
            'total_pages': (total_count + limit - 1) // limit,
            'current_page': page,
            'documents': documents
        })
    else:
        return jsonify({'error': 'Collection not found'}), 404

@app.route('/characters/<character_id>', methods=['GET'])
def get_character_by_id(character_id):
        collection = db[character_collection]
        try:
            character_id = str(character_id)

            query = {'_id': character_id}
            character = collection.find_one(query)

            if character:
                # Convert ObjectId to string for JSON serialization
                character['_id'] = str(character['_id'])
                return jsonify(character)
            else:
                return jsonify({'error': 'Character not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/episodes', methods=['GET'])
def get_episodes(collection_name=episode_collection):
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        total_count = get_total_documents_count(collection_name)
        skip = (page - 1) * limit
        documents = []
        for doc in collection.find().skip(skip).limit(limit):
            # Convert ObjectId to string for JSON serialization
            doc['_id'] = str(doc['_id'])
            documents.append(doc)

        return jsonify({
            'total_pages': (total_count + limit - 1) // limit,
            'current_page': page,
            'documents': documents
        })
    else:
        return jsonify({'error': 'Collection not found'}), 404

@app.route('/episodes/<episode_id>', methods=['GET'])
def get_episode_by_id(episode_id):
        collection = db[episode_collection]
        try:
            episode_id = ObjectId(episode_id)

            query = {'_id': episode_id}
            character = collection.find_one(query)

            if character:
                character['_id'] = str(character['_id'])
                return jsonify(character)
            else:
                return jsonify({'error': 'Episode not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
