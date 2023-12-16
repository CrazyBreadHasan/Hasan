import os
import requests
import html
import random
import RPi.GPIO as GPIO
import time
from time import sleep
import drivers
from os import system
from roatary import RotaryEncoder

clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP) #okok
display = drivers.Lcd()

global punten
counter = 0
punten = 0
goed = 0
fout = 0

def long_string(display, text='', num_line=1, num_cols=16):


    if len(text) > num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i + num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(1)
    else:
        display.lcd_display_string(text, num_line)

def switch_event(event):
    global counter

    if event == RotaryEncoder.CLOCKWISE:
        counter += 1
        if counter in range(0, 5):
            long_string(display, "pepper1", 2)

        elif counter in range(6, 10):
            long_string(display, text = "pepper2",num_line= 2)
        elif counter in range(11, 15):
            long_string(display, "pepper3", 2)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        counter -= 1

    elif event == RotaryEncoder.BUTTONDOWN:
        if counter in range(0, 5):
            long_string(display, "Jatoch", 2)

        elif counter in range(6, 10):
            long_string(display, text="Komt goed", num_line= 2)
        elif counter in range(11, 15):
            print("Red")
        elif counter in range(16, 20):
            print("Yellow")
    elif event == RotaryEncoder.BUTTONUP:
        print("Button up")
    counter = max(0, min(20, counter))

    print(counter)

if __name__ == '__main__':
    encoder_instance = RotaryEncoder(17, 18, 4, switch_event)
    event = encoder_instance.getSwitchState(clk)
    switch_event(event)