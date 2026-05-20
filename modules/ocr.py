import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(img):

    try:
        return pytesseract.image_to_string(
            img,
            lang="eng"
        )

    except Exception as e:
        return f"OCR error: {str(e)}"
