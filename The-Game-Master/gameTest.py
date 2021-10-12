import time
import random

work = 0
varA = 0
varB = 0

def varthing():
    global varA
    varA = varA + 1

def math():
    numA =  random.randint(1, 1000)
    numB =  random.randint(1, 1000)
    numAstr = str(numA)
    numBstr = str(numB)
    anwser = numA + numB
    print(anwser)
    question = input("Wat is " + numAstr + " + " + numBstr + "? ")
    anwserFrom = int(question)
    anwser = numA + numB
    if anwserFrom == anwser:
        varthing()

print("Je loopt in de stad en ziet een auto die je heel erg mooi vind, het is de Fiat multipla!")
time.sleep(3)
print("Je rent naar huis en zoekt op hoe duur je nieuwe droom auto is.")
time.sleep(3)
print("...€19.195")
time.sleep(1.5)
print("Dat is duurder dan verwacht, je kijkt gelijk op je bankrekening en ziet dat je €19.105 mist.")
time.sleep(3)
print("Hoe kan je snel geld verdienen? ")
time.sleep(2)
print("Werken natuurlijk maar dat zal zo lang duren")
time.sleep(3)
print("En dan krijg je het beste idee ooit")
time.sleep(3)
print("Een bank overval!")
time.sleep(3)

def workOrRobberyFunc():
    workOrRobbery = input("Wat wil je gaan doen? \nA=Werken \nB=Bankoverval \n").lower()
    if workOrRobbery == "a":
        work = input("Waar wil je werken? \nA=Donimos \nB=KFC \n").lower()
        time.sleep(1)
        if work == "a":
            print("Je gaat naar Donimos om te solliciteren")
            time.sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            time.sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            math()
            math()
            math()
        elif work == "b":
            print("Je gaat naar KFC om te solliciteren")
            time.sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            time.sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            math()
            math()
            math()
        else:
            print("Dat ging niet helemaal goed we beginnen opnieuw")
            workOrRobberyFunc()
        if varA == 3:
            time.sleep(2)
            print("Dat ging heel erg goed! je bent aangenomen je krijgt via mail te horen wanneer je begint")
            time.sleep(2)
            print("2 uurtjes later kreeg je te horen dat je morgen 17:30 kon beginnen")
            time.sleep(2)
            print("Na een paar jaar werken en sparen heb je eindelijk het geld verzameld")
            time.sleep(2)
            print("Je hebt nu je droom auto gekocht, maar wat nu?")
            time.sleep(2)
            print("Een rijbewijs...")
        elif varA != 3:
            print("Jammer het is niet gelukt je bent niet aangenomen.")
            time.sleep(2)
            print('Je zegt tegen jezelf "Dan toch maar de bank overvallen"')
    elif workOrRobbery == "b":
                        print("ha")
    else:
        print("Dat ging niet helemaal goed probeer het nog eens")
        workOrRobberyFunc()

        


workOrRobberyFunc()

