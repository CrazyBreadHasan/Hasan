import os

import requests
import html
import random
import RPi.GPIO as GPIO
# from thonny.plugins.micropython.generic_api_stubs.pyb import LCD

import time
from time import sleep
import drivers
from os import system
from roatary import RotaryEncoder
clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

display = drivers.Lcd()

global punten
counter = 0
punten = 0
goed = 0
fout = 0

def switch_event(event):
    global counter

    if event == RotaryEncoder.CLOCKWISE:
            counter += 1
            if counter in range (0, 5):
                long_string(display, "pepper1", 2)
            elif counter in range (6, 10):
                long_string(display, "pepper2", 2)
            elif counter in range (11, 15):
                long_string(display, "pepper3", 2)
    elif event == RotaryEncoder.ANTICLOCKWISE:
            counter -= 1

    elif event == RotaryEncoder.BUTTONDOWN:
        if counter in range (0, 5):
            print("Peper")
            long_string(display, "Pepper", 2)
        elif counter in range (6, 10):
            print("Green")
        elif counter in range (11, 15):
            print("Red")
        elif counter in range (16,20):
            print("Yellow")
    elif event == RotaryEncoder.BUTTONUP:
            print("Button up")
    counter = max(0, min(20, counter))

    print(counter)


def encoder():
    counter = 0

    clklaststate = GPIO.input(clk)
    dtlaststate = GPIO.input(dt)


    last_interrupt_time = 0


    DEBOUNCE_TIME = 0.1
    while True:
        clkstate = GPIO.input(clk)
        dtstate = GPIO.input(dt)
        if clkstate != clklaststate or dtstate != dtlaststate:

            current_time = time.time()

            if current_time - last_interrupt_time > DEBOUNCE_TIME:

                if clkstate != dtlaststate:
                    counter += 1
                else:
                    counter -= 1

                counter = max(0, min(20, counter))
                print(counter)

                if counter in range(0, 6):
                    if GPIO.input(clk) == True:
                        # and (GPIO.input(clk, GPIO.LOW))):
                        print("Hello")


            last_interrupt_time = current_time

        clklaststate = clkstate
        dtlaststate = dtstate
        sleep(0.010)





# vragen ophalen
def vragen_ophalen(amount: int, category: int) -> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

def temp_print(val: str):
    print(val)
    time.sleep(1)
    system('cls' if os.name == 'nt' else 'clear')


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

def led_aan_rood():
    for i in range(5):
        GPIO.output(4, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(4, GPIO.LOW)

        time.sleep(0.25)
def led_aan_rood1():
    GPIO.output(4, GPIO.HIGH)

def punten_led():
    global punten

    if punten == -1:
        GPIO.output(4, GPIO.HIGH)
    elif punten == -2:
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
def led_aan_groen():
    for i in range(5):
        GPIO.output(17, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(17, GPIO.LOW)

        time.sleep(0.25)

# vragen mixen
def vragen_mixen(keuze: list) ->list:
    random.shuffle(keuze)
    return keuze


# antwoorden printen
def print_keuzes(keuzes: list) -> None:
    for keuze_index, keuze in enumerate(keuzes):
        print(f"{keuze_index+1}. {html.unescape(keuze)}")

# antwoord van gebruiker
def pak_gebruiker_keuze() -> int:
    while True:
        gebruiker_keuze = int(input("Voer nummer van je keuze in: "))
        if gebruiker_keuze in range(1, 5):
            return gebruiker_keuze - 1
        else:
            print("Invalide antwoord, Voer nummer van je keuze in.")

# spel spelen
def speel_spel(amount: int, catogory: int, encoder_instance: RotaryEncoder) -> None:
    global punten
    global counter
    ophalen = vragen_ophalen(amount, catogory)
    for vraag in ophalen:
        vraag_text = html.unescape(vraag["question"])
        long_string(display, vraag_text, 1)
        keuzes = vraag["incorrect_answers"]
        keuzes.extend([vraag["correct_answer"]])
        mix_vragen = vragen_mixen(keuzes)


        print_keuzes(mix_vragen)

        event = encoder_instance.getSwitchState(clk)
        switch_event(event)
        # encoder()
        geb_keuze_index = pak_gebruiker_keuze()
        geb_keuze_tekst = mix_vragen[geb_keuze_index]
        juiste_antwoord_tekst = html.unescape(vraag["correct_answer"])



        if geb_keuze_tekst == juiste_antwoord_tekst:
            temp_print(long_string(display, "Correct", 2))
            # long_string(display, "Juist", 2)
            display.lcd_clear()

            led_aan_groen()
            punten +=1



        elif geb_keuze_tekst != juiste_antwoord_tekst:
            temp_print(long_string(display, "incorrect", 2))
            # long_string(display, "Incorrect", 2)
            display.lcd_clear()
            led_aan_rood()
            punten -= 1

            punten_led()






if __name__ == '__main__':

    try:
        # encoder()
        amount = 3
        category = 18
        clk = 17
        dt = 18
        encoder_instance = RotaryEncoder(17, 18, 4, switch_event)
        speel_spel(amount, category, encoder_instance)
        print(punten)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Cleaning up GPIO.")
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
        display.lcd_clear() #ok