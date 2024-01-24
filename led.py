#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
# loop through 5 times
for i in range(5):
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    print("Led is on!")
    time.sleep(0.25)

    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    print("Led if off")
    time.sleep(0.25)


GPIO.cleanup()