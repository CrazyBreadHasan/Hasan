import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

for i in range(20):
    print(GPIO.input(4))
    time.sleep(1)  # Hier kun je aangeven hoe lang je wilt wachten tussen elke meting

GPIO.cleanup()