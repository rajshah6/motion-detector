import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for easier viewing
    frame = cv2.flip(frame, 1)
    # Convert to HSV for color filtering (tuned for a certain skin-like range)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 40, 60], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Largest contour is assumed to be the hand
        c = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(c)
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)

        # Here you can add logic to count fingers or detect specific patterns
        # for sign language gestures.

    cv2.imshow("Sign Language Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()