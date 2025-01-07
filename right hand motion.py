import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    roi = frame[100:400, 100:400]
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([20, 255, 255])
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5,5)import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    roi = frame[100:400, 100:400]
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([20, 255, 255])
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5,5), 100)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        
        hull = cv2.convexHull(cnt)
        
        cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
        cv2.drawContours(roi, [hull], -1, (0,0,255), 3)
    
    cv2.rectangle(frame, (100,100), (400,400), (0,255,0), 2)
    
    cv2.imshow('Finger Motion Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows(), 100)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        
        hull = cv2.convexHull(cnt)
        
        cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
        cv2.drawContours(roi, [hull], -1, (0,0,255), 3)
    
    cv2.rectangle(frame, (100,100), (400,400), (0,255,0), 2)
    
    cv2.imshow('Finger Motion Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
