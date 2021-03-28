from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

# Hello Camera
print("Hello Camera")
camera.start_preview()
sleep(100)
camera.stop_preview()
