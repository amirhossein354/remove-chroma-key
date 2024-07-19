import cv2
import numpy as np

cap = cv2.VideoCapture("green-screen.mp4")
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low = np.array([30, 50, 50])
        high = np.array([50, 255, 255])
        mask = ~cv2.inRange(frame, low, high)
        mask = cv2.merge([mask, mask, mask])
        result = cv2.bitwise_and(frame, mask)
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        cv2.imshow('result', result)
        key = cv2.waitKey(5)
        if key != -1:
            print("video quited")
            break
    else:
        print("video finished")
        break
cv2.destroyAllWindows()
cap.release()
