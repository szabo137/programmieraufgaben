"""
*******************
zufallswort.py
*******************

Erzeugt eine gegebene Anzahl an Zufallsworten einer gegebenen maximalen
Laenge aus einem gegebenen Alphabet.


Hauptmodul: mutant.py

"""

import random as r

def zufallswort(maxL,abc):
    """
    gibt ein Zufallswort der maximalen Laenge I:maxL
    aus dem Alphabet I:abc zurueck.
    """
    L=r.randint(1,maxL)
    temp=""
    for index in range(L):
        temp=temp + str(abc[r.randint(0,len(abc)-1)])
    return temp

def zufallswoerter(anz,maxL,abc):
    """
    gibt ein Array aus Zufallsworten zurueck
    """
    temp=[]
    for i in range(anz):
        temp.append(zufallswort(maxL,abc))
    return temp

if __name__ == "__main__":
    anzahl=15
    maximalL=10
    alphabet="0"
    #"abcdefghijklmnopqrstuvwxyz"

    print zufallswoerter(anzahl,maximalL,alphabet)
