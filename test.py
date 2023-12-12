import RPi.GPIO as GPIO
import time

# Set the mode and configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# Turn on the light

for i in range(3):
    GPIO.output([4, 17], [GPIO.HIGH, GPIO.HIGH])
    time.sleep(1)
    # GPIO.output(4, GPIO.LOW)
    # time.sleep(0.25)


GPIO.cleanup()