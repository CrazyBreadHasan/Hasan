import sys
import time

from roatary import RotaryEncoder

PIN_A = 17 # Pin 8
PIN_B = 18 # Pin 10
BUTTON = 4 # Pin 7

def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        print("Clockwise")
    elif event == RotaryEncoder.ANTICLOCKWISE:
        print("Anticlockwise")
    elif event == RotaryEncoder.BUTTONDOWN:
        print("Button down")
    elif event == RotaryEncoder.BUTTONUP:
        print("Button up")
    return

rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,self.switch_event)

while True:
 for counter in range(120):
    print(counter)
    time.sleep(2.0)