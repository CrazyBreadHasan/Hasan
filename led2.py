import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

for i in range(10):

    GPIO.output(4, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.PWM(21, 1000)
    time.sleep(0.25)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)



    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(17, GPIO.LOW)


    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(16, GPIO.LOW)
#ok



GPIO.cleanup()