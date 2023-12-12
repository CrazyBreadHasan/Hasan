import RPi.GPIO as GPIO
import time

# Set the mode and configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Turn on the light

while True:
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(17, GPIO.LOW)