import easyocr

reader = easyocr.Reader(['en'])


def perform_ocr(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)