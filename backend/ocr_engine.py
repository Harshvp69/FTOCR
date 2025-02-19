import pytesseract
import cv2
from PIL import Image
import numpy as np
import os

# Set Tesseract path (ONLY for Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """Enhance image for better OCR accuracy."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)[1]  # Apply thresholding
    return image

def extract_text(image_path):
    """Extract text from image using Tesseract OCR."""
    try:
        if not os.path.exists(image_path):
            print(f"⚠ File not found: {image_path}")
            return None

        # Preprocess image
        processed_image = preprocess_image(image_path)
        pil_image = Image.fromarray(processed_image)

        # Extract text
        text = pytesseract.image_to_string(pil_image)
        return text.strip()
    except Exception as e:
        print(f"❌ OCR Error: {e}")
        return None
