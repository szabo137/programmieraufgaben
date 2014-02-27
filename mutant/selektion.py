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
def guetelaenge(testwort,zielwort,gewicht):
    """
    Gibt die Guete der Laenge mit der Wichtung I:gewicht zurueck
    """
    delta=int(abs(len(testwort)-len(zielwort)))
    Glan=1.0
    for i in range(delta):
        Glan-=1.0/float(len(zielwort))/float(gewicht)
        print Glan
        if Glan < 1.0/float(len(zielwort)):
            Glan=0
            break
    return Glan


# Guetepruefung der korrekten Buchstaben

def pruefAnz(bstbe,wort):
    """
    Prueft wie oft I:bstbe in I:wort enthalten ist
    und gibt die Anzahl zurueck.
    """
    temp=0
    for el in wort:
        if bstbe == el:
            temp+=1
    return temp
    
def gueteKorr(testwort,zielwort,gewicht):
    """
    Gibt die Guete der korrekten Buchstaben mit einer 
    Wichtung von I:gewicht zurueck.
    """
    Gkorr=1.0
    if len(zielwort)<len(testwort):
        temp=testwort
    else:
        temp=zielwort
    for el in temp:
        tempDelta=abs(pruefAnz(el,zielwort) - pruefAnz(el,testwort))
        Gkorr-=tempDelta/float(len(zielwort))/float(gewicht)
        print Gkorr
        if Gkorr < 1.0/float(len(zielwort)):
            Gkorr=0
            break
    return Gkorr

if __name__ == "__main__":
    ziel="mutant"
    #"mutantenmutantenmutantenmutantenmutanten"
    test=str(raw_input("Welches Wort soll geprueft werden? "))
    print "Die Guete -korrekter Buchstabe- betraegt: " + str(gueteKorr(test,ziel,1))