# PPE-Kit-Detection-using-ESP32-Camera-Module
A PPE kit detection project was undertaken by deploying a YOLO model on an ESP32 camera module. C
ompliance response was demonstrated by actuating a servo motor connected to an Arduino Uno, which rotated 90 degrees for 5 seconds upon kit detection. 
This served as a proof-of-concept, illustrating how a deployed flap gate would open on an actual construction site, granting workers entry

## Hardware Requirements
* Arduino Uno
* ESP32-CAM Module
* ESP32-CAM-MB Micro USB Download Module (or ESP32-CAM programmer)
* Servo Motor
* Jumper wires for connections

## Software Requirements
* Arduino IDE
* Editor for Python script

## Required Connections  
* The ESP32 cam module has to be pressed on the MB board for conneting all the pins
NOTE: Arduino Uno and the ESP32 module are both connected to the laptop directly via USB cables each

**Arduino Uno with Servo Motor:** 
   <img width="425" alt="Circuit_Diagram_Arduino_Servo" src="https://github.com/user-attachments/assets/2b6ef5bb-0ea6-43d6-bc7f-a7a7a96a37ab" />

## Code Deployment
* Upload the given Servo motor Arduino IDE code after setting up the above circuit
* **Note:** You might face driver issues with this cam module, in case you do, install the CH340 driver manually from a browser before uploading the ESP32 Arduino IDE code
* Upload the given ESP32 Arduino IDE code on the ESP32
* Once both codes are uploaded successfully and verified, run the main.py file






