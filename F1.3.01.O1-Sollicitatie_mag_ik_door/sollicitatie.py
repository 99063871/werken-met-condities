print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('+        Sollicitatieformulier "Circusdirecteur"       +')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

name = input("Wat is uw naam? ")
experience = int(input("Heeft u praktijk ervaring met 1 van het volgende: dieren-dressuur, jongleren of acrobatiek? kies 1, 2 of 3(zo niet kies dan 0) "))

if experience == 1:
    experienceJob = int(input("Hoeveel jaar ervaring heeft u met dieren-dressuur? "))
    if experienceJob > 4:
        experienceQualify = "ja"

elif experience == 2:
    experienceJob = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
    if experienceJob > 5:
        experienceQualify = "ja"

elif experience == 3:
    experienceJob = int(input("Hoeveel jaar ervaring heeft u met acrobatiek? "))
    if experienceJob > 3:
        experienceQualify = "ja"
else:
    experienceQualify = "nee"

diploma = input("Bezit u over een MBO-4 ondernemen diploma? (Ja/Nee) " ).lower()
license = input("Bezit u over een geldig vrachtwagen rijbewijs? (Ja/Nee) ").lower()
fakequestion1 = input("Waar heeft u uw rijbewijs vandaan? ")
hat = input("bezit u over een hoge hoed? (Ja/Nee) ").lower()
fakequestion2 = input("Draagt u de hoed vaak? ")

manOrFemale = input("Bent u een man of vrouw? M/V ").lower()
if manOrFemale == "m":
    mustache = int(input("Hoe breed is uw snor?(in centimeters invullen) "))
    if mustache > 10:
        manOrFemale = "ja"
elif manOrFemale == "v":
    redHair = int(input('Draagt u rood krulhaar? Zo ja hoe lang is het?(lengte invullen en als u geen rood krulhaar heeft "0" invullen '))
    if redHair > 20:
        manOrFemale = "ja"
else:
    manOrFemale = "false"

height = int(input("Wat is uw lichaamslengte? "))
fakequestion3 = input("Wat is uw lievelings eten? ")
weight = int(input("Wat is uw lichaamsgewicht? "))
certificate = input('Bezit u over het certificaat "Overleven met gevaarlijk personeel"? (Ja/Nee) ').lower()
fakequestion4 = input("Heeft een broer/zus?(vul in 'ja ik heb... of nee ")

print("Beste " + name + ",")
if experienceQualify == "ja" and diploma == "ja" and license == "ja" and hat == "ja" and manOrFemale == "ja" and height > 150 and weight > 90 and certificate == "ja":
    print("Gefeliciteerd!!! U komt in aanmerking voor een sollicitatiegesprek")

else:
    print("Helaas, u komt niet in aanmerking voor een sollicitatiegesprek. Maar als u denkt dat u ergens iets verkeerd hebt ingevuld kunt u het opnieuw proberen")