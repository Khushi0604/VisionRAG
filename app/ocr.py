import easyocr
import pytesseract

reader = easyocr.Reader(['en'])

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def perform_ocr(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)