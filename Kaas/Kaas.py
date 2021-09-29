Yellow = input("Is de kaas geel? ").lower()

if Yellow == "ja":
    YellowHole = input("Zitten er gaten in? ").lower()

    if YellowHole == "ja":
        HoleExpensive = input("Is de kaas belachelijk duur? ").lower()

        if HoleExpensive == "ja":
            print("Emmenthaler")
        elif HoleExpensive == "nee":
            print("Leerdammer")

    elif YellowHole == "nee":
        NHoleHard = input("Is de kaas hard als steen? ").lower()

        if NHoleHard == "ja":
            print("Pammigiano Reggiano")

        elif NHoleHard == "nee":
            print("Goudse kaas") 

elif Yellow == "nee":
    NYellowMold = input("Heeft de kaas blauwe schimmels? ").lower()

    if NYellowMold == "ja":
        MoldCrust = input("Heeft de kaas een korst? ").lower()

        if MoldCrust == "ja":
            print("Bleu de Rochbaron")
        
        elif MoldCrust == "nee":
            print("Foume d'Amber")
    elif NYellowMold == "nee":
        NMoldCrust = input("Heeft de kaas een korst? ").lower()
        if NMoldCrust == "ja":
            print("Camembert")

        elif NMoldCrust == "nee":
            print("Mozzarella")