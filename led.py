#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(13, GPIO.OUT)
# loop through 5 times
for i in range(5):
    GPIO.output(13, GPIO.HIGH)
    print("Led is on!")
    time.sleep(0.25)

    GPIO.output(13, GPIO.LOW)
    print("Led if off")
    time.sleep(0.25)


GPIO.cleanup()