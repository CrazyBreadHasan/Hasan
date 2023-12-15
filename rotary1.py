import sys
import time

from roatary import RotaryEncoder

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

rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)

while True:
 for counter in range(120):
    print(counter)
    time.sleep(2.0)