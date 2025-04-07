import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
d
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        success, image = cap.read()
        if not success:
            break

        # Convert the image color for processing
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, 
                                                  results.multi_handedness):
                label = handedness.classification[0].label
                # Index finger tip is landmark 8
                index_finger_tip = hand_landmarks.landmark[8]
                if label == 'Right':
                    # Simple check if index finger tip exists in frame
                    if 0 < index_finger_tip.x < 1 and 0 < index_finger_tip.y < 1:
                        cv2.putText(image, 'INDEX FINGER DETECTED', (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Frame', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()