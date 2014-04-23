"""
*******************
selektion.py
*******************

Fuehrt Selektionsprozess an gegebenen Worten aus. Dabei sollen verschiedene
Gueten geprueft werden:

    Laenge des Strings
    Anzahl korrekter Buchstaben
    Anzahl korrekter Positionen

Das Modul gibt dann die besten 50 Prozent der Eingangsworte zurueck.

Hauptmodul: mutant.py

"""


# Guetepruefung der Laenge
def gueteLaenge(testwort,zielwort,gewicht=1.0):
    """
    Gibt die Guete der Laenge mit der Wichtung I:gewicht zurueck
    """
    delta=int(abs(len(testwort)-len(zielwort)))
    Glan=1.0
    for i in range(delta):
        Glan-=1.0/float(len(zielwort))/float(gewicht)
        if Glan < 1.0/float(len(zielwort)):
            Glan=0
            break
    return Glan


# Guetepruefung der korrekten Buchstaben

def pruefAnz(bstbe,wort):
    """
    Prueft wie oft I:bstbe in I:wort enthalten ist
    und gibt die Anzahl zurueck.

    TODO:
    Vll mit string.count() verbessern!!
    mglw. unter verwendung von string.remove()
    """
    temp=0
    for el in wort:
        if bstbe == el:
            temp+=1
    return temp

def gueteKorr(testwort,zielwort,gewicht=1.0):
    """
    Gibt die Guete der korrekten Buchstaben mit einer
    Wichtung von I:gewicht zurueck.
    """
    # gewicht=5 ist ein guter wert
    Gkorr=1.0
    if len(zielwort)<len(testwort):
        temp=testwort
    else:
        temp=zielwort
    for el in temp:
        tempDelta=abs(pruefAnz(el,zielwort) - pruefAnz(el,testwort))
        Gkorr-=tempDelta/float(len(zielwort))/float(gewicht)
        if Gkorr < 1.0/float(len(zielwort)):
            Gkorr=0
            break
    return Gkorr


# Guetepruefung der korrekten Position von Buchstaben

def guetePos(testwort, zielwort, gewicht=1):
    """
    Gibt die Guete der korrekten Position von Buchstaben mit einer
    Wichtung von I:gewicht zurueck.
    """
    Gpos=0.0
    if len(zielwort)>len(testwort):
        temp=testwort
    else:
        temp=zielwort
    for i in range(len(temp)):
        if zielwort[i] == testwort[i]:
            Gpos+=1/float(len(zielwort))/float(gewicht)
    return Gpos


# Selektion der Wortliste

def selektion(testliste, zielwort,gewicht=[1.0, 1.0, 1.0]):
    """
    Fuehrt die Selektion nach den Kriterien:
        Laenge
        Buchstaben
        Position
    durch und gibt die besten 50 Prozent wider.
    """
    #Fuellen eines dicts mit (wort:bewertung)
    bewertung={}
    for wort in testliste:
        bewertung[wort]=gueteLaenge(wort, zielwort, gewicht[0]) + gueteKorr(wort, zielwort, gewicht[1])+ guetePos(wort, zielwort, gewicht[2])

    #sortieren des dicts nach den Bewertungen
    bestenliste=[]
    temp=sorted(bewertung.items(), key=lambda item:item[1], reverse=True)
    for el in temp:
        bestenliste.append(el[0])

    #Ausgabe der besten 50 Prozent (aufgerundet)
    return bestenliste[:int(len(bestenliste)/2.0 + 0.5)]


if __name__ == "__main__":
    ziel="mutant"
    #"mutantenmutantenmutantenmutantenmutanten"
    test=['qjdgatxozw', 'dgw', 'gazye', 'p', 'kcwcsdkkp', 'vxi', 'rjvdn', 'ijxnoc', 'domvomcrx', 'kiqji', 'irkhun', 'ki', 'ghoyiwvvip', 'zs', 'pn', "muat","mutant"]
    print "Die Bestenliste ist also: ",selektion(test,ziel,[3.0,5.0,5.0])
