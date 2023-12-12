#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)