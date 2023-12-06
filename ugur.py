import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

status = 1
been_pressed = 0

while status == 1:
    if GPIO.input(4) == 0 and been_pressed == 0:
        print("Been pressed")
    elif been_pressed == 1 and GPIO.input(4)  == 1:
        print("Been released")
        time.sleep(0.5)
        status = 0

gpio.cleanup()