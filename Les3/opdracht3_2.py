leeftijd = int(input("Geef je leeftijd: "))
paspoort = str(input("Nederlands paspoort: "))
if leeftijd >= 18 and paspoort.lower() == "ja":
    print("Gefeliciteerd, Je mag stemmen!")