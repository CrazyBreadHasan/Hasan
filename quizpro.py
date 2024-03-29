import requests
import html
import random
import RPi.GPIO as GPIO
import time
import json

global punten
punten = 0
goed = 0
fout = 0
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(26, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# vragen ophalen
def vragen_ophalen(json_file_path: str) -> list:
    with open (json_file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data["results"]

def led_aan_rood():
    for i in range(5):
        GPIO.output(26, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(26, GPIO.LOW)

        time.sleep(0.25)
def led_aan_rood1():
    GPIO.output(4, GPIO.HIGH)

def punten_led():
    global punten

    if punten == -1:
        GPIO.output(26, GPIO.HIGH)
    elif punten == -2:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
def led_aan_groen():
    for i in range(5):
        GPIO.output(19, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(19, GPIO.LOW)

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
def speel_spel(amount: int, catogory: int) -> None:
    global punten
    ophalen = vragen_ophalen(amount, catogory)
    for vraag in ophalen:
        vraag_text = html.unescape(vraag["question"])
        print(vraag_text)
        keuzes = vraag["incorrect_answers"]
        keuzes.extend([vraag["correct_answer"]])
        mix_vragen = vragen_mixen(keuzes)
        print_keuzes(mix_vragen)
        geb_keuze_index = pak_gebruiker_keuze()
        geb_keuze_tekst = mix_vragen[geb_keuze_index]
        juiste_antwoord_tekst = html.unescape(vraag["correct_answer"])
        if geb_keuze_tekst == juiste_antwoord_tekst:
            print("Juist!!!. ")
            led_aan_groen()
            punten +=1



        elif geb_keuze_tekst != juiste_antwoord_tekst:
            print("incorrect")
            led_aan_rood()
            punten -= 1

            punten_led()






if __name__ == '__main__':
    amount = 3
    category = 18
    speel_spel(amount, category)
    print(punten)