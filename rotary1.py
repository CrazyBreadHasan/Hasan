import RPi.GPIO as GPIO
import time

from RPi import GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = max(0, min(20, counter)) # clip the counter to 0 to 20

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
            # check if enough time has passed since the last interrupt
            if current_time - last_interrupt_time > DEBOUNCE_TIME:
                # update the counter
                if clkstate == 0 and dtstate == 1:  # if the pins are in this state, it means clockwise rotation
                    counter += 1
                # else: # ignore the other states, as they mean counter-clockwise rotation
                #     pass
                print(counter)

                # add the if statement to limit the counter range
                if counter < 0:  # if the counter is below the minimum
                    counter = 0  # reset it to 0
                elif counter > 20:  # if the counter is above the maximum
                    counter = 20  # reset it to 20

            # update the last interrupt time
            last_interrupt_time = current_time

        clklaststate = clkstate  # update the previous states
        dtlaststate = dtstate
        sleep(0.001)
finally:
    GPIO.cleanup()