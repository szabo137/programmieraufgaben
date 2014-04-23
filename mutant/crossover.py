"""
*******************
crossover.py
*******************

Fuehrt fuer gegebene Wortliste elementweise einen Crossover durch und erzeugt
damit eine neue Wortliste mit doppelt so vielen Worten.

Hauptmodul: mutant.py

"""

#import random as r
from random import sample as rsample
from random import randint as rrandint

def erstelleSeq(Aeins,Anull):
    """
    Erstellt eine Sequenz der Laenge I:Aeins aus Einsen und Nullen,
    welche zufaellig auf die Sequenz verteilt werden. Dabei ist die
    Anzahl der Nullen eine zufaellige Zahl zwischen 1 und I:Anull
    """
    if Aeins < Anull:
        print "!!!FALSCHE ANORDNUNG DER WORTE!!!"
    indexe=rsample(range(Aeins), rrandint(1,Anull))

    seq=[]
    for i in range(Aeins):
        seq.append(1)

    for el in indexe:
        seq[el] = 0

    return seq


def erstelleKind(papa,mama):
    """
    Erzeugt mit Hilfe von Crossover ein Kind-String aus den beiden
    Input-Strings.
    """
    if len(papa) > len(mama):
        lang=papa
        kurz=mama
    else:
        lang=mama
        kurz=papa
    Seq=erstelleSeq(len(lang), len(kurz))

    kind=""
    for index in range(len(lang)):
        if Seq[index]:
            kind+=lang[index]
        else:
            kind+=kurz[0]
            kurz=kurz[1:]

    return str(kind)

def crossover(altGen,anz):
    neuGen=[]
    for i in range(anz):
        paar=rsample(range(len(altGen)),2)
        kind=erstelleKind(altGen[paar[0]],altGen[paar[1]])
        neuGen.append(kind)
    return neuGen

if __name__ == "__main__":
    wortliste=['gaqn', 'zbvfpz']

    print crossover(wortliste,4)
