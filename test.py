import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)

GPIO.output(17, GPIO.HIGH)
time.sleep()

# Add a delay or other code here if needed

# Cleanup GPIO settings when done
GPIO.cleanup()