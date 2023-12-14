import RPi.GPIO as GPIO
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

try:
    while True:
        clkstate = GPIO.input(clk)
        dtstate = GPIO.input(dt)
        if clkstate != clklaststate:
            if dtstate != clklaststate:
                counter += 1
            else:
                counter -= 1
            print(counter)

        clklaststate = clkstate
        sleep(0.001)
finally:
    GPIO.cleanup()