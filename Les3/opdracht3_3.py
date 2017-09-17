leeftijd = int(input("Geef je leeftijd: "))
paspoort = str(input("Nederlands paspoort (ja/nee): "))
if leeftijd >= 18 and paspoort.lower() == "ja":
    print("Gefeliciteerd, Je mag stemmen!")
else:
    print("Jammer man, geen stemrecht voor jou!")
