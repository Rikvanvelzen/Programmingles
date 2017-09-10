print("Dit is opdracht 1_2")
print("-" * 40)
#A. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
s1 = "Supercalifragilisticexpialidocious"
print("Antwoord A is", len(s1))
print("-" * 40)
#De string is in de variabel opgeslagen. Door middel van len(s) te gebruiken leest hij de lengte van de opgeslagen string.
# Die 34 verschillende karakters gebruikt.
#--------------------------------------------------------------
#B. Komt in 'Supercalifragilisticexpialidocious 'de tekst 'ice' voor?
antwoordB = "ice" in s1
print("Het antwoord van vraag B is", antwoordB)
print("-" * 40)
#De functie ‘’in’’ kijkt of de eerste string die is ingevuld aanwezig is in de complete string.
# Hier op geeft hij een Boolean terug namelijk true or false.
#---------------------------------------------------------------------------------------
#C. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
s2 = "Honorificabilitudinitatibus"
antwoordC = len(s1) > len(s2)
print("Het antwoord van vraag C is", antwoordC)
print("-" * 40)
#Hier stop ik de strings in een makkelijk te herkennen variabel die code schoon houd.
# Vervolgens laat ik het programma berekenen of de lengte van s1 groter is dan s2.
#-----------------------------------------------------------------------
#D. Welke componist komt in alfabetische volgorde het eerst: '
# Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?
antwoordDA = min('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
antwoordDB = max('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
print("De eerste in volgorde is", antwoordDA + ", de laatste is in volgorde", antwoordDB)
print("-" * 40)
#Python leest vergelijkingen van strings op alfabetische volgorde.
# Dus wanneer en omdat het programma met min() en max() alle mogelijkheden met elkaar vergelijkt kan ik
#  zo zien we volgens alfabetische volgorde eerste en laatste is.