from elasticsearch import Elasticsearch
import uuid

# Connect to Elasticsearch (Use the container name inside Docker)
ES_HOST = "http://elasticsearch:9200"
es = Elasticsearch(ES_HOST)

INDEX_NAME = "ftocr"

def init_index():
    """Initialize Elasticsearch index if it does not exist."""
    try:
        if not es.indices.exists(index=INDEX_NAME):
            print(f"📌 Creating index: {INDEX_NAME}")
            es.indices.create(index=INDEX_NAME, body={
                "mappings": {
                    "properties": {
                        "image_id": {"type": "keyword"},
                        "image_path": {"type": "text"},
                        "extracted_text": {"type": "text"}
                    }
                }
            })
            print("✅ Index created successfully!")
        else:
            print("✅ Index already exists.")
    except Exception as e:
        print(f"❌ Error initializing index: {e}")

def insert_data(image_path, extracted_text):
    """Insert OCR results into Elasticsearch."""
    doc_id = str(uuid.uuid4())
    doc = {
        "image_id": doc_id,
        "image_path": image_path,  # Ensure correct path format
        "extracted_text": extracted_text
    }

    print(f"📌 Trying to insert: {doc}")

    try:
        response = es.index(index=INDEX_NAME, id=doc_id, body=doc)
        print(f"✅ Insert successful! Response: {response}")
    except Exception as e:
        print(f"❌ Insert failed: {e}")

def search_images(query):
    """Search images by extracted text and return formatted paths."""
    print(f"🔍 Searching for: {query}")

    try:
        response = es.search(index=INDEX_NAME, body={
            "query": {
                "match_phrase": {  # Better accuracy with phrase search
                    "extracted_text": query
                }
            }
        })

        results = [
            {"image_path": f"/view-image/{hit['_source']['image_path'].split('/')[-1]}"}
            for hit in response["hits"]["hits"]
        ]

        if results:
            print(f"✅ Search Results Found: {results}")
        else:
            print("⚠ No matching results found.")

        return results

    except Exception as e:
        print(f"❌ Search failed: {e}")
        return []
