import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

for i in range(10):

    if GPIO.input(22) == True:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(4, GPIO.LOW)
    elif GPIO.input(22) == False:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(17, GPIO.LOW)

GPIO.cleanup()