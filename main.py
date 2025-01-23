from ultralytics import YOLO
import cv2
import time
import urllib.request  # url requests (opening urls)
import numpy as np
import serial  # serial communication with external devices
# URL of the ESP32-Cam's video stream
url = "http://192.168.58.193/cam-mid.jpg"
# 5-second delay before camera turns on
time.sleep(5)
# video capture object
cap = cv2.VideoCapture(url)
# YOLO model
model = YOLO("best-2.pt")
# serial connection
ser = serial.Serial('COM9', 9600)
# boolean variable to keep track of detection
detected = False
rotation_active = False  # To track servo rotation is active or not
while True:
    img_resp = urllib.request.urlopen(url)  # retrieve image from feed
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)  # convert to numpy array
    frame = cv2.imdecode(imgnp, -1) # decode using opencv's imdecode function
    results = model.predict(source=frame, show=True)
    if len(results[0]) > 0:  # Objects detected
        if not detected and not rotation_active:
            detected = True
            rotation_active = True
            ser.write(b'90\n')  # Send angle command to Arduino
            time.sleep(5)  # Rotate for 5 seconds
            ser.write(b'0\n')  # Send angle command to Arduino
            time.sleep(1)  # Wait for servo to return
            rotation_active = False
    else:
        detected = False
    cv2.imshow("Object Detection", frame)  # display the frame with the detected objects
    if cv2.waitKey(1) & 0xFF == ord('q'):  # loop breaks if the 'q' key is pressed
        break
# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
