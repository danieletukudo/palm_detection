import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
# First step is to initialize the Hands class an store it in a variable
mp_hands = mp.solutions.hands

# Now second step is to set the hands function which will hold the landmarks points
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.3)

# Last step is to set up the drawing function of hands landmarks on the image
mp_drawing = mp.solutions.drawing_utils


while True:
    success, image = cap.read()
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image_height, image_width, _ = image.shape

    if results.multi_hand_landmarks:

        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            
        
        
              
            print(f'{mp_hands.HandLandmark(20).name}:') 
            print(f'x: {hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x * image_width}')
            print(f'y: {hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y * image_height}')
            print(f'z: {hand_landmarks.landmark[mp_hands.HandLandmark(20).value].z * image_width}n')
                    
        mp_drawing.draw_landmarks(image = image, landmark_list = hand_landmarks,
                                        connections = mp_hands.HAND_CONNECTIONS)



    cv2.imshow("Output", image)
    cv2.waitKey(1)
