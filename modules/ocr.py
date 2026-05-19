import pytesseract
def extract_text(img):
    return pytesseract.image_to_string(img)
