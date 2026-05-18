import fitz
import os
import pandas as pd
from PIL import Image
import pytesseract
from docx import Document

UPLOAD_DIR = "uploads"


def extract_pdf_text(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def extract_pdf_images(file_path):
    doc = fitz.open(file_path)
    image_paths = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"page_{page_index+1}_{img_index}.{image_ext}"
            image_path = os.path.join(UPLOAD_DIR, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths


def extract_docx_text(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_csv_text(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()


def extract_image_text(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)