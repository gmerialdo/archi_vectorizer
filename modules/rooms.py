import cv2
def detect_rooms(img):
    contours,_=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    rooms=[]
    for c in contours[:10]:
        x,y,w,h=cv2.boundingRect(c)
        if w>100 and h>100:
            rooms.append({"bbox":[int(x),int(y),int(w),int(h)]})
    return rooms
