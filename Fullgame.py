import os
import requests
import html
import random
from random import shuffle
import RPi.GPIO as GPIO
import time
from time import sleep
import drivers
from os import system
from roatary import RotaryEncoder
import json

clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # okok
GPIO.setup(5, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
global vraag_type


def vragen_ophalen(json_file_path: str) -> list:
    with open(json_file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data["results"]



def vragen_mixen(keuze: list) -> list:
    random.shuffle(keuze)
    return keuze


def print_keuzes(keuzes: list, type_vraag) -> str:
    global keuze1, keuze2, keuze3, keuze4
    choices_string = ""

    for keuze_index, keuze in enumerate(keuzes):
        choices_string += f"{keuze_index + 1}. {html.unescape(keuze)}\n"

    if type_vraag == "multiple":
        keuze1 = choices_string.split("\n")[0]
        keuze2 = choices_string.split("\n")[1]
        keuze3 = choices_string.split("\n")[2]
        keuze4 = choices_string.split("\n")[3]
    elif type_vraag == "boolean":
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


def pak_gebruiker_keuze_rotary(encoder_instance: RotaryEncoder, event, type_vraag) -> int:
    global counter, keuze1, keuze2, keuze3, keuze4
    button_pressed = False
    print("Please fill in your answer: ")
    while button_pressed == False:
        # print(encoder_instance.getSwitchState(clk))
        if GPIO.input(4) == GPIO.LOW:
            button_pressed = True
            # if type_vraag == "multiple": #ok
            if counter in range(0, 5):
                return 0  # Index for keuze1
            elif counter in range(6, 10):
                print("Answer 2")
                return 1  # Index for keuze2
            elif counter in range(11, 15):
                return 2  # Index for keuze3
            elif counter in range(16, 20):
                return 3  # Index for keuze4 #ok1
        elif GPIO.input(22) == GPIO.LOW:

            GPIO.cleanup()
            os.system("sudo shutdown -h now")



    print("Too late")
    # Return a default index (0) if event is not BUTTONDOWN


# def pak_gebruiker_keuze_rotary(encoder_instance: RotaryEncoder, event, type_vraag) -> int:
#     global counter, keuze1, keuze2, keuze3, keuze4
#
#     if event == RotaryEncoder.BUTTONDOWN:
#         print("Button pressed")
#         if type_vraag.__eq__("multiple"):
#             if counter in range(0, 5):
#                 return keuze1
#             elif counter in range(6, 10):
#                 return keuze2
#             elif counter in range(11, 15):
#                 return keuze3
#             elif counter in range(16, 20):
#                 return keuze4


def speel_spel(vragen: list, encoder_instance: RotaryEncoder, type_vraag) -> str:
    global goed
    global fout
    global counter
    global vraag_type

    led_uit()
    shuffle(vragen)

    for vraag in vragen[:5]:
        type_vraag = vraag["type"]
        vraag_text = html.unescape(vraag["question"])
        long_string(display, vraag_text, 1)
        keuzes = vraag["incorrect_answers"]
        keuzes.extend([vraag["correct_answer"]])
        mix_vragen = vragen_mixen(keuzes)

        keuze_text = print_keuzes(mix_vragen, type_vraag)
        print(keuze_text)
        # long_string(display, text=keuze_text, num_line=2)

        event = encoder_instance.getSwitchState(clk)
        switch_event(event, type_vraag)
        vraag_type = type_vraag

        # encoder()
        geb_keuze_index = pak_gebruiker_keuze_rotary(encoder_instance, event, type_vraag)
        print(geb_keuze_index)
        geb_keuze_tekst = mix_vragen[geb_keuze_index]
        juiste_antwoord_tekst = html.unescape(vraag["correct_answer"])

        if geb_keuze_tekst == juiste_antwoord_tekst:
            temp_print(long_string(display, text="Correct", num_line=2))
            # long_string(display, "Juist", 2)
            display.lcd_clear()

            goed += 1



        elif geb_keuze_tekst != juiste_antwoord_tekst:
            temp_print(long_string(display, "incorrect", 2))
            # long_string(display, "Incorrect", 2)
            display.lcd_clear()

            fout += 1

        punten_led()


    return juiste_antwoord_tekst, type_vraag


def switch_event(event, type_vraag):
    global counter, vraag_type, keuze1, keuze2, keuze3, keuze4

    if event == RotaryEncoder.CLOCKWISE:
        counter += 1
    elif event == RotaryEncoder.ANTICLOCKWISE:
        counter -= 1

    if type_vraag == "multiple":
        if counter in range(0, 5):
            return keuze1
        elif counter in range(6, 10):
            return keuze2
        elif counter in range(11, 15):
            return keuze3
        elif counter in range(16, 20):
            return keuze4

    # elif event == RotaryEncoder.BUTTONUP:
    #     return

    counter = min(20, max(0, counter))
    if vraag_type == "multiple":
        display.lcd_clear()
        if counter in range(1, 5):
            display.lcd_clear()
            long_string(display, text=keuze1, num_line=2)
        elif counter in range(6, 10):
            display.lcd_clear()
            print("Counter is in the range (6, 10)")
            long_string(display, text=keuze2, num_line=2)
        elif counter in range(11, 15):
            display.lcd_clear()
            long_string(display, text=keuze3, num_line=2)
        elif counter in range(16, 20):
            display.lcd_clear()
            long_string(display, text=keuze4, num_line=2)
    elif vraag_type == "boolean":
        display.lcd_clear()
        if counter in range(0, 5):
            display.lcd_clear()
            long_string(display, "True", 2)
        elif counter in range(6, 10):
            display.lcd_clear()
            long_string(display, "False", 2)
        elif counter in range(11, 15):
            display.lcd_clear()
            print("True")
        elif counter in range(16, 20):
            display.lcd_clear()
            print("False")

    print(counter)
    print(vraag_type)


def long_string(display, text='', num_line=1, num_cols=16):
    if len(text) > num_cols:

        display.lcd_display_string(text[:num_cols], num_line)
        sleep(0.1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i + num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(0.5)
    else:
        display.lcd_display_string(text, num_line)


def punten_led():
    global goed, fout

    if goed == 1:
        GPIO.output(26, GPIO.HIGH)
    elif goed == 2:
        GPIO.output(13, GPIO.HIGH)
    elif goed == 3:
        GPIO.output(19, GPIO.HIGH)
    if fout == 1:
        GPIO.output(16, GPIO.HIGH)
    elif fout == 2:
        GPIO.output(20, GPIO.HIGH)
    elif fout == 3:
        GPIO.output(21, GPIO.HIGH)


def uitstlag():
    global goed, fout
    if goed >= 3:
        long_string(display, text="De deur gaat open, De code is 7", num_line=1)
    elif fout >= 3:
        long_string(display, text="De deur is voor altijd opslot", num_line=2)


def led_uit():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)


def temp_print(val: str):
    print(val)
    time.sleep(1)
    system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    try:
        # encoder()
        json_file_path = "/home/pi/Hasan/vragen.json" #
        vragen = vragen_ophalen(json_file_path)
        amount = 5
        category = 18
        clk = 17
        dt = 18
        encoder_instance = RotaryEncoder(17, 18, 4, switch_event)

        speel_spel(vragen, encoder_instance, type_vraag="multiple")

        print(goed)
        print(fout)
        time.sleep(5)
        uitstlag()
        led_uit()





    except KeyboardInterrupt:
        print("Keyboard interrupt. Cleaning up GPIO.")
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
        display.lcd_clear()  # ok
        os.system("sudo shutdown -h now")