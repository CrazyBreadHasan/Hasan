#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(4, GPIO.OUT)
# loop through 50 times
for i in range(50):
    GPIO.output(4, GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(4, GPIO.LOW)
    time.sleep(0.025)

GPIO.cleanup