"""
*******************
mutation.py
*******************

Fuer eine gegebene Wortliste sollen einige Worte einer Mutation unterworfen
werden. Die Mutation ist hierbei das hinzufuegen, entfernen oder Veraendern
eines beliebigen Buchstabens.

Hauptmodul: mutant.py

"""

from random import randint as rrandint
from random import sample as rsample

def mutWort(wort,abc):
    """
    Zufaellig soll eine Mutation an I:wort ausgefuehrt werden. Die Mutationen
    sind hierbei:
        Entfernen eines beliebigen Buchstabens
        Hinzufuegen eines bel. Buchstabens aus I:abc
        Austauschen eines bel. Buchstabens durch einen aus I:abc
    """

    #Auswahl der Mutationsmethode
    meth=rrandint(1,3)
    #Auswahl der Position
    pos=rrandint(0,len(wort)-1)
    #Auswahl des zufaelligen Buchstabens
    zufBstbe=abc[rrandint(0,len(abc)-1)]
    if meth==0:
        #Einfuegen
        temp=wort.replace(wort[pos],wort[pos] + zufBstbe )
    elif meth==1:
        #Entfernen
        if len(wort)==1:
            temp=wort
        else:
            temp=wort.replace(wort[pos],"")
    else:
        #Austauschen
        temp=wort.replace(wort[pos],zufBstbe)

    return temp


def mutation(Gen,abc,anteil=0.3):
    """
    Fuehrt eine Mutation der Individuen der Generation I:Gen aus dem Alphabet
    I:abc mit einer Wahrscheinlichkeit von I:anteil durch
    """
    auswahl=rsample(range(len(Gen)),int(len(Gen)*anteil))
    for el in auswahl:
        Gen[el]=mutWort(Gen[el],abc)
    return Gen



if __name__ == "__main__":
   vorher=['toyimmg', 'iu', 'njyy', 'fldmlcl', 'xdt', 'oifv', 'a', 'zlbdicdy', 'idebqrfrow', 'uvb']
   alphabet="abcdefghijklmnopqrstuvwxyz"
   print vorher
   print mutation(vorher,alphabet)
