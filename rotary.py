import RPi.GPIO as GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0  # Start at 0
clkLastState = GPIO.input(clk)

# Define a callback function that updates the counter
def update_counter(channel):
    global counter, clkLastState
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
        print(counter)
        # If the counter has reached 20, exit the program
        if counter == 20:
            GPIO.cleanup()
            exit()
    clkLastState = clkState

# Add event detection to the clk and dt pins
GPIO.add_event_detect(clk, GPIO.BOTH, callback=update_counter)
GPIO.add_event_detect(dt, GPIO.BOTH, callback=update_counter)

# Wait for the user to press Ctrl+C
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()