import time
import random

def varthing():
    global varA
    varA = varA + 1
    print(varA)

def math():
    numA =  random.randint(1, 1000)
    numB =  random.randint(1, 1000)
    numAstr = str(numA)
    numBstr = str(numB)
    question = input("Wat is " + numAstr + " + " + numBstr + "? ")
    anwserFrom = int(question)
    anwser = numA + numB
    if anwserFrom == anwser:
        print("goed gedaan kut")
        varthing()

work = 0
varA = 0
varB = 0

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

def workOrRobberyfunc():
    workOrRobbery = input("Wat wil je gaan doen? \nA=Werken \nB=Bankoverval \n").lower()
    if workOrRobbery == "a":
        work = input("Waar wil je werken? \nA=Donimos \nB=KFC \n").lower()
        time.sleep(1)

workOrRobberyfunc()

if work == "a":
    print("Je gaat naar Donimos om te solliciteren")
    time.sleep(2)
    print("Je hebt geluk en je kan gelijk een gesprek hebben!")
    time.sleep(2)
    print("Ik ga je een paar reken vragen stellen")
    math()
    math()
    math()







