#importeer GPIO en time package
import RPi.GPIO as GPIO
import time
#gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)
#zet de pin als output
p = GPIO.PWM(4, 1000)

def playTone(duration)
    p.start(50)
    time.sleep(duration)
    p.stop()


playTone(0.2)

GPIO.cleanup()