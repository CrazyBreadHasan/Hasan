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
def pak_gebruiker_keuze(event):
    if event == RotaryEncoder.BUTTONDOWN:
        print("Button")



pak_gebruiker_keuze(event =RotaryEncoder.BUTTONDOWN)