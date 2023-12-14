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
dtlaststate = GPIO.input(dt)

# add a variable to store the last interrupt time
last_interrupt_time = 0

# add a constant to define the minimum time between interrupts
DEBOUNCE_TIME = 0.01  # in seconds

try:
    while True:
        clkstate = GPIO.input(clk)
        dtstate = GPIO.input(dt)
        if clkstate != clklaststate or dtstate != dtlaststate:  # check both pins for changes
            # get the current time
            current_time = time.time()

            if current_time - last_interrupt_time > DEBOUNCE_TIME:
                # update the counter
                if clkstate != dtlaststate:
                    counter += 1
                else:
                    counter -= 1

                counter = max(0, min(20, counter))
                print(counter)





            last_interrupt_time = current_time

        clklaststate = clkstate
        dtlaststate = dtstate
        sleep(0.010)
finally:
    GPIO.cleanup()