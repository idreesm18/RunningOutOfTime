from src import camera as camera_module
import matplotlib.image
import numpy as np
import time

if __name__ == '__main__':
    # Initialize the camera
    camera = camera_module.Camera({
        "show_preview": False
    })

    # Capture an image
    camera.capture()
    time.sleep(2)
    print(type(camera.image_array))
    print(camera.image_array)
    # Generate a filename based on the current timestamp
    matplotlib.image.imsave('monkey.png', camera.image_array)
	
    print(f"Image saved as monkey")
