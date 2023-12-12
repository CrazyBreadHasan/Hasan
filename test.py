import RPi.GPIO as GPIO
import time

# Set the mode and configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

# Turn on the light
GPIO.output(4, GPIO.HIGH)

# Add a delay or other code here if needed

# Cleanup GPIO settings when done
GPIO.cleanup()