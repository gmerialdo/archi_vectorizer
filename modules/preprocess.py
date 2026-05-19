import fitz,cv2,numpy as np
def pdf_to_image(pdf,dpi=300):
    doc=fitz.open(pdf)
    p=doc[0]
    pix=p.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72))
    img=np.frombuffer(pix.samples,dtype=np.uint8)
    img=img.reshape(pix.height,pix.width,pix.n)
    return cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

def clean(img):
    _,th=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th
