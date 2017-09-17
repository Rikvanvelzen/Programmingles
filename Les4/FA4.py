def standaardprijs(afstandKM):
    if afstandKM >= 50:
        return 15 + 0.6 * afstandKM
    elif afstandKM < 0:
        return 0
    else:
        return afstandKM * 0.8

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    ritprijs_value = 0
    weekendrit = 'ja'
    if leeftijd < 12 or leeftijd >= 65:
        ritprijs_value += standaardprijs(afstandKM) * 0.70
        return print(round(ritprijs_value,2))
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        ritprijs_value += standaardprijs(afstandKM) * 0.65
        return print(round(ritprijs_value,2))
    elif leeftijd >= 12 or leeftijd < 65 and weekendrit == True:
        ritprijs_value += standaardprijs(afstandKM) * 0.60
        return print(round(ritprijs_value,2))

standaardprijs(120)
ritprijs(15, 'Ja', 120)