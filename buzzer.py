import RPi.GPIO as GPIO
import time
# Use BCM mode for the pin numbering (conform breakout)
GPIO.setmode(GPIO.BCM)
# Set the pin as output
GPIO.setup(4, GPIO.OUT)
p= GPIO.PWM(4, 1000)

def playTone(duration):
    p.start(50)
    time.sleep(duration)
    p.stop()

try:
    # Play a tone for half a second
    playTone(0.5)
finally:
    # Clean up the GPIO pins
    GPIO.cleanup()