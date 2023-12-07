import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(17, GPIO.OUT)

for i in range(10):
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.5)


    GPIO.output(4, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.5)


GPIO.cleanup()