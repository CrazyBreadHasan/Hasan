import RPi.GPIO as GPIO
import time

# Set the mode and configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Turn on the light
GPIO.output(17, GPIO.HIGH)

# Add a delay or other code here if needed

# Cleanup GPIO settings when done
GPIO.cleanup()