import cv2
from src import led as led_module
from src import vehicle as vehicle_module
from src import motor as motor_module
from picamera2 import Picamera2
import time
import numpy as np

face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
# cv2.startWindowThread()

picam2 = Picamera2()
# # picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

led1 = led_module.LED({
        "pin": 20
    })

# motor1 = motor_module.Motor({
#     "pins": {
#         "speed": 13,
#         "control1": 5,
#         "control2": 6
#     }
# })

# motor2 = motor_module.Motor({
#     "pins": {
#         "speed": 12,
#         "control1": 7,
#         "control2": 8
#     }
# })

vehicle = vehicle_module.Vehicle(
        {
            "motors": {
                "left": {
                    "pins": {
                        "speed": 13,
                        "control1": 5,
                        "control2": 6
                    }
                },
                "right": {
                    "pins": {
                        "speed": 12,
                        "control1": 7,
                        "control2": 8
                    }
                }
            }
        }
    )

first_face_seen = False

while True:

    
    if first_face_seen:
        vehicle.pivot_right(1)
        time.sleep(3)
    led1.on()
    speed_right_min = 2.5
    speed_right_max = 3.5
    speed_left_min = speed_right_min * 0.8
    speed_left_max = speed_right_max * 0.8

    speeds_right = list(np.linspace(speed_right_min, speed_right_max, 15)) 
    speeds_left = list(np.linspace(speed_left_min, speed_left_max, 15)) 

    dt = 0.25
    # motor1.stop()
    # motor2.stop()
    # vehicle.stop()
    # time.sleep(dt)

    for speed_right, speed_left in zip(speeds_right, speeds_left):
        vehicle.drive_forward()
        time.sleep(dt)

    vehicle.drive_forward(1)
    time.sleep(1.5)
    vehicle.drive(0.5, True, 1, True)
    time.sleep(5)
    vehicle.drive_forward(1)
    time.sleep(3)
    vehicle.drive(1, True, 0.5, True)
    time.sleep(5)
    vehicle.drive_forward(1)
    time.sleep(1.5)

    vehicle.stop()
    first_face_seen = True
    led1.off()
        
#         led2.on()
#     # for (x, y, w, h) in faces:
#     #     cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

#     cv2.imshow("Camera", im)
#     cv2.waitKey(1)