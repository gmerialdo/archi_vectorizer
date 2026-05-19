import cv2,numpy as np
def detect_walls(img):
    lines=cv2.HoughLinesP(img,1,np.pi/180,100,minLineLength=80,maxLineGap=15)
    out=[]
    if lines is None:
        return []
    for l in lines:
        x1,y1,x2,y2=l[0]
        out.append({"start":[int(x1),int(y1)],"end":[int(x2),int(y2)]})
    return out
