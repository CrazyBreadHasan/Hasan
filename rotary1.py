import RPi.GPIO as GPIO
from time import sleep

counter = 0 # define a counter variable
Enc_A = 17 # define the GPIO pin for the CLK pin of the encoder
Enc_B = 18 # define the GPIO pin for the DT pin of the encoder

GPIO.setmode(GPIO.BCM) # set the GPIO mode to BCM
GPIO.setup(Enc_A, GPIO.IN) # set the CLK pin as input
GPIO.setup(Enc_B, GPIO.IN) # set the DT pin as input

clklaststate = GPIO.input(Enc_A) # get the initial state of the CLK pin

try:
    while True: # loop forever
        clkstate = GPIO.input(Enc_A) # get the current state of the CLK pin
        dtstate = GPIO.input(Enc_B) # get the current state of the DT pin
        if clkstate != clklaststate: # if the CLK pin state has changed, the encoder is being rotated
            if dtstate != clkstate: # if the DT pin state is different from the CLK pin state, it means clockwise rotation
                counter += 1 # increment the counter
            else: # if the DT pin state is the same as the CLK pin state, it means counter-clockwise rotation
                counter -= 1 # decrement the counter
            print(counter) # print the counter value

        clklaststate = clkstate # update the previous state of the CLK pin
        sleep(0.001) # add a small delay to avoid bouncing
except KeyboardInterrupt: # if the user presses Ctrl+C, exit the program
    GPIO.cleanup() # clean up the GPIO pins