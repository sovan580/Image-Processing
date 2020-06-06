import cv2
import numpy as np

def angledetector(x):

    img =  cv2.imread(x)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(blured, cv2.HOUGH_GRADIENT, 1, 20,param1=50,param2=20,minRadius=0,maxRadius=20)
    detected_circles = np.uint16(np.around(circles))    
    a = np.array([int (detected_circles[0][0][0]),int (detected_circles[0][0][1])])
    b = np.array([int (detected_circles[0][1][0]),int (detected_circles[0][1][1])])
    c = np.array([int (detected_circles[0][2][0]),int (detected_circles[0][2][1])]) 
    b = b - a
    c = c - a
    a = 0  
    ba = b - a
    ca = c - a
    cosine_angle = np.dot(ba,ca) / ( np.linalg.norm(ba) * np.linalg.norm(ca))
    angle = np.arccos(cosine_angle)
    d = np.degrees(angle)
    print('{:.2f}'.format(d))
    for (x ,y ,r) in detected_circles[0, :]:
        cv2.circle(img, (x,y), r, (255,0,0),3)
        cv2.circle(img, (x,y), 2, (255,0,0),3)
    cv2.imshow('output',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
angledetector('image_1.png')
angledetector('image_2.png')
angledetector('image_3.png')
