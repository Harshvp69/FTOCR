# Use an official Python runtime as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install Tesseract OCR
RUN apt update && apt install -y tesseract-ocr

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
