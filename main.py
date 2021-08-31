import cv2
from cvzone.HandTrackingModule import HandDetector
from keyboard import keys, Button
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

finalText = ""

# Creating Button Objects
btns = []
for i, keyList in enumerate(keys):
    for j, key in enumerate(keyList):
        btns.append(Button(((Button.btnInitPos[0] + Button.size[0] + Button.btnPadding) * j, (Button.btnInitPos[1] + Button.size[1] + Button.btnPadding) * i), key))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detecting Hands
    img = detector.findHands(img)

    # Detecting fingers positions using MediaPipe (cvzone) library
    lmList, bboxInfo = detector.findPosition(img)

    # Drawing buttons
    for btn in btns:
        if lmList:
            resp = btn.action(detector, lmList, img)
            if resp:
                finalText += resp
                sleep(0.15)
        btn.draw(img)

        cv2.rectangle(img, (0, 500), (1280, 600), Button.btnColor, cv2.FILLED)
        cv2.putText(img, finalText, (30, 550), cv2.FONT_HERSHEY_PLAIN, 3, Button.textColor, 4)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        break