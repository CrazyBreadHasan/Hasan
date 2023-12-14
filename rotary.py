mport RPi.GPIO as GPIO
import time

from RPi import GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0

clklaststate = GPIO.input(clk)
dtlaststate = GPIO.input(dt)

try:
    while True:
        clkstate = GPIO.input(clk)
        dtstate = GPIO.input(dt)
        if clkstate != clklaststate or dtstate != dtlaststate: # check both pins for changes
            if clkstate != dtlaststate: # if they are different, it means clockwise rotation
                counter += 1
            else: # if they are the same, it means counter-clockwise rotation
                counter -= 1
            print(counter)

        clklaststate = clkstate # update the previous states
        dtlaststate = dtstate
        sleep(0.001)
finally:
    GPIO.cleanup()