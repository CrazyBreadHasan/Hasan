import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if GPIO.input(22) == True:
            GPIO.output(4, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(4, GPIO.LOW)

        elif GPIO.input(22) == False:
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(17, GPIO.LOW)

except KeyboardInterrupt:
    print("Keyboard interrupt. Cleaning up GPIO.")
    GPIO.cleanup()

finally:
    GPIO.cleanup()