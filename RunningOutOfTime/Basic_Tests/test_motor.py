import numpy as np
from src import motor as motor_module
import time
import random

if __name__ == '__main__':

    motor1 = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    motor2 = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        }
    })

    # total_time = 30
    # interval = 10

    # start_time = time.time()

    # while (time.time() - start_time) < total_time:
    #     # Perform your action here

    #     right_speed = random.uniform(0.25, 0.75)
    #     left_speed = random.uniform(0.25, 0.75)

    #     speeds_right = list(np.linspace(right_speed, right_speed + 0.25, 5))
    #     speeds_left = list(np.linspace(left_speed, left_speed + 0.25, 5))


    #     dt = 0.25
    #     motor1.stop()
    #     motor2.stop()
    #     time.sleep(dt)

    #     for right_speed, left_speed in zip(speeds_right, speeds_left): 
    #         motor1.forward(right_speed)
    #         motor2.forward(left_speed)
    #     # Wait for the specified interval

    #     motor1.stop()
    #     motor2.stop()
    #     time.sleep(interval)


    speed_right_min = 2.5
    speed_right_max = 3.5
    speed_left_min = speed_right_min * 0.8
    speed_left_max = speed_right_max * 0.8

    speeds_right = list(np.linspace(speed_right_min, speed_right_max, 15)) 
    speeds_left = list(np.linspace(speed_left_min, speed_left_max, 15)) 

    dt = 0.25
    motor1.stop()
    motor2.stop()
    time.sleep(dt)

    for speed_right, speed_left in zip(speeds_right, speeds_left):
        motor1.forward(speed_right)
        motor2.forward(speed_left)
        time.sleep(dt)

    # for speed in speeds:
    #     print('Motor forward at {}% speed'.format(speed * 100))
    #     motor1.forward(speed)
    #     motor2.forward(speed)
    #     time.sleep(dt)

    # for i in range(20):
    #     motor1.forward(0.5)
    #     motor2.forward(0.5)

    # for speed in speeds2:
    #     print('Motor backward at {}% speed'.format(speed * 100))
    #     motor1.forward(speed)
    #     motor2.forward(speed)
    #     time.sleep(dt)

    motor1.stop()
    motor2.stop()
