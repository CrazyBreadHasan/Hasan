import RPi.GPIO as GPIO
import time

# Set the mode and configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

# Turn on the light

for i in range(5):
    GPIO.output(4, GPIO.HIGH)
    time.sleep(150)
    # GPIO.output(4, GPIO.LOW)
    # time.sleep(0.25)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(150)

GPIO.cleanup()