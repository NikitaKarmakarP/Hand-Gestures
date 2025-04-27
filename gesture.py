import cv2
import mediapipe as mp

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Previous gesture to avoid multiple prints
prev_gesture = None

def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    fingers = []

    # Check for fingers
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Check for thumb
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 2].x:
        fingers.append(1)
    else:
        fingers.append(0)

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb)

    gesture_text = ""

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            fingers = count_fingers(hand_landmarks)
            total_fingers = fingers.count(1)

            # Detect gesture
            if total_fingers == 0:
                gesture_text = "OK"
            elif total_fingers == 1:
                if fingers[0] == 1:
                    gesture_text = "1"
                else:
                    gesture_text = "Thumbs Up (Best of Luck)"
            elif total_fingers == 2:
                gesture_text = "2"
            elif total_fingers == 3:
                gesture_text = "3"
            elif total_fingers == 4:
                gesture_text = "4"
            elif total_fingers == 5:
                gesture_text = "5"

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Only print if gesture changes
            if gesture_text != prev_gesture and gesture_text != "":
                print(f"Detected Gesture: {gesture_text}")
                prev_gesture = gesture_text

    # Display gesture text
    if gesture_text:
        cv2.putText(frame, gesture_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0, 0, 255), 3, cv2.LINE_AA)

    # Show frame
    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
