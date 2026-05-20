from modules.preprocess import pdf_to_image,clean
from modules.walls import detect_walls
from modules.ocr import extract_text
from modules.rooms import detect_rooms

def process(pdf_path):
    img=pdf_to_image(pdf_path)
    img=clean(img)

    walls=detect_walls(img)
    rooms=detect_rooms(img)
    try:
        text = extract_text(img)
    except Exception:
        text = "OCR unavailable"

    return {
        "walls":walls[:20],
        "rooms":rooms,
        "ocr_preview":text[:300]
    }
