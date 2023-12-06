import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

been_pressed = 0


while True:
    if GPIO.input(4) == 0 and been_pressed == 0:
        print("Je kan op een knop klikken (wooow)")
    elif been_pressed == 1 and GPIO.input(4) == 1:
        print("Been released")
        time.sleep(0.5)
        break

GPIO.cleanup()