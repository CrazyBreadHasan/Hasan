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
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # okok
display = drivers.Lcd()

global punten
counter = 0
punten = 0
goed = 0
fout = 0
global keuze1
global keuze2
global keuze3
global keuze4


def vragen_ophalen(amount: int, category: int) -> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]


def vragen_mixen(keuze: list) -> list:
    random.shuffle(keuze)
    return keuze


def print_keuzes(keuzes: list, type_vraag) -> str:
    global keuze1, keuze2, keuze3, keuze4
    choices_string = ""

    for keuze_index, keuze in enumerate(keuzes):
        choices_string += f"{keuze_index + 1}. {html.unescape(keuze)}\n"

    if (type_vraag.__eq__("multiple")):
        keuze1 = choices_string.split("\n")[0]
        keuze2 = choices_string.split("\n")[1]
        keuze3 = choices_string.split("\n")[2]
        keuze4 = choices_string.split("\n")[3]
    elif (type_vraag.__eq__("boolean")):
        keuze1 = choices_string.split("\n")[0]
        keuze2 = choices_string.split("\n")[1]

    return choices_string


def pak_gebruiker_keuze() -> int:
    while True:
        gebruiker_keuze = int(input("Voer nummer van je keuze in: "))
        if gebruiker_keuze in range(1, 5):
            return gebruiker_keuze - 1
        else:
            print("Invalide antwoord, Voer nummer van je keuze in.")





def speel_spel(amount: int, catogory: int, encoder_instance: RotaryEncoder, type_vraag) -> None:
    global punten
    global counter
    ophalen = vragen_ophalen(amount, catogory)

    for vraag in ophalen:
        type_vraag = vraag["type"]
        vraag_text = html.unescape(vraag["question"])
        long_string(display, vraag_text, 1)
        keuzes = vraag["incorrect_answers"]
        keuzes.extend([vraag["correct_answer"]])
        mix_vragen = vragen_mixen(keuzes)

        keuze_text = print_keuzes(mix_vragen, type_vraag)
        print(keuze_text)
        long_string(display, text=keuze_text, num_line=2)

        event = encoder_instance.getSwitchState(clk)
        switch_event(event, type_vraag)
        # encoder()
        geb_keuze_index = pak_gebruiker_keuze()
        geb_keuze_tekst = mix_vragen[geb_keuze_index]
        juiste_antwoord_tekst = html.unescape(vraag["correct_answer"])

        if geb_keuze_tekst == juiste_antwoord_tekst:
            temp_print(long_string(display, text="Correct", num_line=2))
            # long_string(display, "Juist", 2)
            display.lcd_clear()

            led_aan_groen()
            punten += 1



        elif geb_keuze_tekst != juiste_antwoord_tekst:
            temp_print(long_string(display, "incorrect", 2))
            # long_string(display, "Incorrect", 2)
            display.lcd_clear()
            led_aan_rood()
            punten -= 1

            punten_led()
        return juiste_antwoord_tekst, type_vraag


def switch_event(event, type_vraag):
    global counter, keuze1, keuze2, keuze3, keuze4

    if event == RotaryEncoder.CLOCKWISE:
        print(type_vraag)
        counter += 1

        if type_vraag.__eq__("multiple"):
            # display.lcd_clear()
            # long_string(display, text=str(counter), num_line=2)
            if counter in range(1, 5):
                display.lcd_clear()
                long_string(display, text=keuze1, num_line=2)
            elif counter in range(6, 10):
                display.lcd_clear()
                print("Counter is in the range (6, 10)")
                long_string(display, text=keuze2, num_line=2)
            elif counter in range(11, 15):
                long_string(display, text=keuze3, num_line=2)
            elif counter in range(16, 20):
                long_string(display, text=keuze4, num_line=2)
        elif type_vraag.__eq__("boolean"):
            if counter in range(0, 5):
                long_string(display, "True", 2)
            elif counter in range(6, 10):
                long_string(display, "False", 2)
            elif counter in range(11, 15):
                print("True")
            elif counter in range(16, 20):
                print("False")

    elif event == RotaryEncoder.ANTICLOCKWISE:
        counter -= 1

    elif event == RotaryEncoder.BUTTONDOWN:
        print("Button pressed")
    if type_vraag.__eq__("multiple"):
        if counter in range(0, 5):
            return keuze1
        elif counter in range(6, 10):
            return keuze2
        elif counter in range(11, 15):
            return keuze3
        elif counter in range(16, 20):
            return keuze4


    elif event == RotaryEncoder.BUTTONUP:
        print("Button released")
        return

    counter = min(20, max(0, counter))
    print(counter)


def long_string(display, text='', num_line=1, num_cols=16):
    if len(text) > num_cols:

        display.lcd_display_string(text[:num_cols], num_line)
        sleep(0.5)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i + num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(0.5)
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


def temp_print(val: str):
    print(val)
    time.sleep(1)
    system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    try:
        # encoder()
        amount = 3
        category = 18
        clk = 17
        dt = 18
        encoder_instance = RotaryEncoder(17, 18, 4, switch_event)

        speel_spel(amount, category, encoder_instance, type_vraag="multiple")
        print(punten)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Cleaning up GPIO.")
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
        display.lcd_clear()  # ok