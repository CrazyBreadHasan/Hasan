import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

for i in range(10):

    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)



    GPIO.output(19, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(19, GPIO.LOW)




    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26, GPIO.LOW)
#ok#ok



GPIO.cleanup()