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
GPIO.cleanup()

def beep(freq, duration):
#frequency in Hz
#duration in seconds
 period = 1.0/freq

def sweep(start_freq, end_freq, duration):
# deze functie start met de start frequentie en
# aan het eind (t + duration) is de frequentie opgelopen
# (of afgenomen) tot de end frequentie
 start_period = 1.0/start_freq
 end_period = 1.0/end_freq
 avg_period = (start_period + end_period) / 2
 freq_delta = (end_freq – start_freq)/avg_period