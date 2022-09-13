import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = True,
max_num_hands =2,
min_detection_confidence = 0.5)
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB) 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(cx,cy)
                if id == 20 :
                        #print ( f'{hands.HandLandmark(id).name}:')
                        print(f'X: {lm.landmark[hands.HandLandmark(20).value].x * w}')
                        print(f'Y: {lm.landmark[hands.HandLandmark(20).value].y * h}')
                        print(f'Z: {lm.landmark[hands.HandLandmark(20).value].z * c}n')

                   # cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", image)
    cv2.waitKey(1)