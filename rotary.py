import RPi.GPIO as GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0  # Start at 0
clkLastState = GPIO.input(clk)

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1

            # Ensure the counter stays within the range [0, 20]
            counter = max(0, min(20, counter))

            # print(counter)
            print(dtState)

            # If the counter has reached 20, exit the loop
            if counter == 20:
                break

        clkLastState = clkState
        sleep(0.01)

finally:
    GPIO.cleanup()