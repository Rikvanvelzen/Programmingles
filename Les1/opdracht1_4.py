print("Dit is Practice Exercise 1_4")
print("-" * 40)
#-----------------------------------------------------------------
#1. Kijk of 6.75 groter is dan a en kleiner dan b uit 1_3.
a = 6
b = 7
antwoord1 = 6.75 > a and 6.75 < b
print("Is het true or false dat antwoord 1 groter is dan a en b?", antwoord1)
print("-" * 40)
#Met de ‘’and’’ functie zorg ik ervoor dat de machine mij verteld of beide gevallen waar zijn.
# Als er maar een waar is resulteert de boodschap in een False.
#--------------------------------------------------------------------------------
#2. Kijk of de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
inventaris = ["papier", "nietjes", "pennen"]
voornaam = "Rik"
tussenvoegsel = "van"
achternaam = "Velzen"
mijnnaam = [voornaam, tussenvoegsel, achternaam]
antwoord2 = inventaris / 5 > mijnnaam
print("Is de lengte van de lijst inventaris groter dan de lijst mijnnaam?", antwoord2)
print("-" * 40)
#Hier vermenigvuldig ik de lijst eerst met 5 keer om vervolgens te kijken of deze groter is dan de lijst mijnnaam.
#-------------------------------------------------------------------------------------------------------------------
#3. Kijk of lijst inventaris leeg is, of juist meer dan 10 items bevat.
isHetLanger = inventaris == 0 or len(inventaris) > 10
print("Is de lijst leeg of is hij groter dan 10 items?", isHetLanger)
#Hier wordt de functie ‘’or’’ gebruikt om te kijken of een van deze twee beweringen klopt.
# Inventaris == 0 kijkt of de inventaris leeg is. len(inventaris) > 10 kijkt of de lijst groter dan 10 is.
# Hierbij wordt de functie len() aangeroepen omdat een lijst niet met een integer kan vergeleken worden.
print("-" * 40)
