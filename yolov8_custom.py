from ultralytics import YOLO
import os
import cv2
from ultralytics.utils.plotting import Annotator, colors
import pygame
import torch
pygame.init()
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO('best.pt')

VIDEO_PATH = "przejazd4.mp4"
sound_to_play = pygame.mixer.Sound('mixkit-alarm-tone-996.wav')
# results = model.track(source=VIDEO_PATH, show=True,conf=0.5, save=True, tracker='bytetrack.yaml')




cap = cv2.VideoCapture(VIDEO_PATH)
cap.set(3, 640)
cap.set(4, 480)


while True:
    ret, img = cap.read()

    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.track(source=img)



    for r in results:
        annotator = Annotator(img)
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
            if len(r.boxes.cls) > 0:
                dclass = r.boxes.cls[0].item()
                print(dclass)
                if dclass == 0.0:
                    sound_to_play.play()

        img = annotator.result()
    cv2.imshow('YOLO V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
