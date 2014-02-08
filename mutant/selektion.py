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

def guetelaenge(testwort,zielwort):
    delta=int(abs(len(testwort)-len(zielwort)))
    Glan=1.0
    for i in range(delta):
        Glan-=1.0/float(len(zielwort))
        print Glan
        if Glan < 1.0/float(len(zielwort)):
            Glan=0
            break
    return Glan


if __name__ == "__main__":
    ziel="mutantenmutantenmutantenmutantenmutanten"
    test=str(raw_input("Welches Testwort soll geprueft werden? "))
    print "Die Guete von " + test + " betraegt: " + str(guetelaenge(test,ziel))