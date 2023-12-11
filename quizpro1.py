import requests
import html
import random
import RPi.GPIO as GPIO
import time

global punten # global variable for points
global totaal # global variable for total questions
punten = 0 # initialize points to zero
totaal = 0 # initialize total to zero
GPIO.setmode(GPIO.BCM)
#zet de pin als output
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# vragen ophalen
def vragen_ophalen(amount: int, category: int) -> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

def led_aan_rood():
    for i in range(5):
        GPIO.output(4, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(4, GPIO.LOW)

        time.sleep(0.25)
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
def speel_spel(amount: int, catogory: int) -> None:
    global punten # use the global variable for points
    global totaal # use the global variable for total questions
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
        correct = False # initialize a boolean variable to track the correctness of the answer
        if geb_keuze_tekst == juiste_antwoord_tekst:
            print("Juist!!!. ")
            led_aan_groen()
            punten += 1 # increment points by one if the answer is correct
            correct = True # set the variable to True if the answer is correct



        elif geb_keuze_tekst != juiste_antwoord_tekst and not correct: # check if the answer is wrong and the user did not get the points
            print("incorrect")
            led_aan_rood()
            punten -= 1 # decrement points by one if the answer is wrong and the user did not get the points
        totaal += 1 # increment total by one for each question
        print(f"Je hebt {punten} punten van de {totaal} vragen.") # print the current score and total questions
    percentage = round((punten / totaal) * 100, 2) # calculate the percentage of correct answers
    print(f"Je hebt het spel afgemaakt en je hebt {punten} punten van de {totaal} vragen. Dat is {percentage}% goed.") # print the final score and percentage


if __name__ == '__main__':
    amount = 3
    category = 18
    speel_spel(amount, category)