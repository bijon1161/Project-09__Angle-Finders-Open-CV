import cv2
import math
path = 'angles.jpg'
img = cv2.imread(path)

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

cv2.imshow('Image',img)
cv2.setMouseCallback('Image',mousePoints)
cv2.waitKey(0)
