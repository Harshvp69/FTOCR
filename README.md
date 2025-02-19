FTOCR: Image OCR & Search Engine

FTOCR is a web application that extracts text from images using Tesseract OCR and stores it in Elasticsearch. Users can upload images, extract text, and search for images based on the extracted text.

Features

- OCR Processing – Extracts text from images using Tesseract OCR.
- Search Functionality – Finds images based on extracted text using Elasticsearch.
- Image Upload Support – Users can upload images and retrieve text.
- Simple and Clean UI – User-friendly interface built with Flask and Bootstrap.
- Dockerized Setup – Easily run the application using Docker.

Installation & Setup

Prerequisites

- Python 3.10 or later
- pip and virtualenv
- Docker and Docker Compose
- Elasticsearch 8.5 or later
- Tesseract OCR

1. Clone the Repository git clone https\://github.com/Harshvp69/FTOCR.git cd FTOCR

2. Setup Virtual Environment & Install Dependencies
   python -m venv ftocr-venv
   source ftocr-venv/bin/activate  # On Windows, use: ftocr-venv\Scripts\activate
   pip install -r requirements.txt

3. Run with Docker (Recommended)
   Ensure Docker is installed and running. Then execute:
   docker-compose up --build

This will start:

- Flask app on localhost:5000
- Elasticsearch on localhost:9200

4. Run Locally (Without Docker)
   Ensure Elasticsearch is running at [http://localhost:9200](http://localhost:9200) before running:
   python app.py

Usage Guide

1. Upload an Image for OCR

- Go to [http://localhost:5000](http://localhost:5000)
- Click Choose File and upload an image.
- Click Extract Text to process the image.
- The extracted text will be displayed.

2. Search for Text in Images

- Enter text in the search box.
- Click Search to find matching images.
- The images containing the text will be displayed.

Project Structure

FTOCR/
│── backend/
│   ├── ocr\_engine.py   # Handles OCR extraction with Tesseract
│   ├── search\_engine.py # Elasticsearch indexing and search logic
│── templates/
│   ├── index.html      # Main UI page
│── static/uploads/     # Folder for uploaded images
│── app.py              # Flask application
│── Dockerfile          # Docker setup
│── docker-compose.yml  # Runs app and Elasticsearch together
│── requirements.txt    # Dependencies
│── README.md           # Project documentation

Troubleshooting

Search Not Working?

- Ensure Elasticsearch is running and accessible at [http://localhost:9200](http://localhost:9200)
- Run the following command to check if images are indexed:
  curl -X GET "[http://localhost:9200/ftocr/\_search?pretty](http://localhost:9200/ftocr/_search?pretty)"
- If no results, try restarting the Elasticsearch container.

OCR Not Working?

- Ensure Tesseract OCR is installed and accessible.
- On Windows, add Tesseract to your system PATH.

Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a branch (git checkout -b feature-name)
3. Commit changes (git commit -m "Added new feature")
4. Push (git push origin feature-name)
5. Open a Pull Request

License

This project is licensed under the MIT License.

Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Tesseract OCR: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Elasticsearch: [https://www.elastic.co/](https://www.elastic.co/)
- Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)

Future Enhancements

- Add user authentication
- Implement pagination for search results
- Improve OCR accuracy with image preprocessing
- Support multi-language OCR

