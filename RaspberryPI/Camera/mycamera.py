from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

# Hello Camera
print("Hello Camera")
camera.start_preview()
sleep(10)
camera.stop_preview()

# Camera Alpha
print("Camera Alpha 200")
camera.start_preview(alpha=200) # Alpha 0 - 255
sleep(10)
camera.stop_preview()

# Camera Image Capture
print("Camera Capture in 5 Seconds")
camera.start_preview(alpha=200)
sleep(5
      )
camera.capture("capture.jpg")
print("Image captured")
camera.stop_preview()

# Camera Series of Images
print("Capturing series of images")
camera.start_preview(alpha=200)
for i in range(5):
    sleep(5)
    camera.annotate_text = "Expert Cyclone 2018" # Add some text
    camera.capture("Image%s.jpg" % i)
    print("image %s captured" % i)
camera.stop_preview()

# Camera Record Video
print("Camera Record Video")
camera.start_preview(alpha=200)
camera.annotate_text = "Expert Cyclone 2018" # Add some text
camera.start_recording("video.h264")
sleep(10)
camera.stop_recording()
camera.stop_preview()
print("video captured")
# play video on terminal "omxplayer video.h264"


# Brightness Setting
print("Brightness Setting")
camera.annotate_background= Color("black")
camera.annotate_foreground= Color("violet")
camera.start_preview()
for i in range(100):
    camera.annotate_text    = "Brightness: %s" % i
    camera.brightness       =  i # 0 - 100
    sleep(0.10)
camera.stop_preview()


# Contrast Setting
print("Constrast Setting")
camera.annotate_foreground = Color("cyan")
camera.annotate_text_size = 50 # 6 - 160 default of 32
camera.start_preview()
for i in range(100):
    camera.annotate_text    = "Constrast: %s" % i
    camera.contrast         =  i # 0 - 100
    sleep(0.10)
camera.stop_preview()


# Camera Effects
print("Camera Effects")
camera.annotate_foreground = Color("red")
camera.annotate_text_size = 50 # 6 - 160 default of 32
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.annotate_text    = "Camera Effect: %s" % effect
    camera.image_effect     = effect  
    camera.capture("Image %s effect.jpg" % effect)
    sleep(2)
camera.stop_preview()
