#from flask import Flask, request, render_template
#import os
#from backend.ocr_engine import extract_text
#from backend.search_engine import init_index, insert_data, search_images

#app = Flask(__name__)
#UPLOAD_FOLDER = "data/"
#app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Initialize Elasticsearch index
#init_index()

#@app.route("/", methods=["GET", "POST"])
#def upload_image():
#    """Handles image upload and text extraction."""
#    if request.method == "POST":
#        image = request.files["image"]
#        if image:
#            filepath = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
#            image.save(filepath)
#            text = extract_text(filepath)
#            insert_data(filepath, text)
#            return f"✅ Text Extracted: {text}"
#    return render_template("upload.html")

#@app.route("/search", methods=["GET"])
#def search():
#    """Handles text-based search for images."""
#    query = request.args.get("q")
#    if query:
#        results = search_images(query)
#        return render_template("search.html", results=results, query=query)
#    return render_template("search.html", results=[])

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000, debug=True)




from flask import Flask, request, render_template, jsonify, url_for
import os
from backend.ocr_engine import extract_text
from backend.search_engine import insert_data, search_images, init_index

app = Flask(__name__)

# Define Upload Directory
UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Initialize Elasticsearch index
init_index()

@app.route("/", methods=["GET", "POST"])
def home():
    """Handles image upload and OCR processing."""
    if request.method == "POST":
        if "image" in request.files:
            image = request.files["image"]
            if image.filename == "":
                return jsonify({"error": "No file selected"})

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(filepath)

            extracted_text = extract_text(filepath)

            if extracted_text:
                insert_data(filepath, extracted_text)

            return jsonify({
                "image_path": url_for('static', filename=f'uploads/{image.filename}'), 
                "extracted_text": extracted_text
            })

    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    """Handles text-based search for images."""
    query = request.form.get("query")
    if not query:
        return jsonify({"error": "No search query provided"})

    results = search_images(query)

    # Convert stored paths to proper Flask URLs for frontend display
    search_data = [{"image_path": url_for('static', filename=f'uploads/{os.path.basename(item["image_path"])}')} for item in results]

    return jsonify({"search_results": search_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
