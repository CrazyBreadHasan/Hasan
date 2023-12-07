#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(4, GPIO.OUT)
# loop through 5 times
for i in range(5):
 print(GPIO.output(4, GPIO.HIGH))
 print("Led is on!")
 time.sleep(0.25)
 print(GPIO.output(4, GPIO.LOW))
 print("Led if off")
 time.sleep(0.25)
GPIO.cleanup()