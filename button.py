import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
# GPIO.setup(22, GPIO.IN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# for i in range(10):
while True:

        if GPIO.input(22) == True:
                GPIO.output(4, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(17, GPIO.LOW)

        elif GPIO.input(22) == False:
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(4, GPIO.LOW)

GPIO.cleanup()