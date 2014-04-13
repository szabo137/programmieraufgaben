"""
*******************
mutation.py
*******************

Fuer eine gegebene Wortliste sollen einige Worte einer Mutation unterworfen
werden. Die Mutation ist hierbei das hinzufuegen, entfernen oder Veraendern
eines beliebigen Buchstabens.

Hauptmodul: mutant.py

"""

import random as r

def mutWort(wort,abc):
    """
    Zufaellig soll eine Mutation an I:wort ausgefuehrt werden. Die Mutationen
    sind hierbei:
        Entfernen eines beliebigen Buchstabens
        Hinzufuegen eines bel. Buchstabens aus I:abc
        Austauschen eines bel. Buchstabens durch einen aus I:abc
    """
    
    #Auswahl der Mutationsmethode
    meth=r.randint(1,3)
    #Auswahl der Position
    pos=r.randint(0,len(wort)-1)
    #Auswahl des zufaelligen Buchstabens
    zufBstbe=abc[r.randint(0,len(abc)-1)]
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
    auswahl=r.sample(range(len(Gen)),int(len(Gen)*anteil+1))
    for el in auswahl:
        Gen[el]=mutWort(Gen[el],abc)
    return Gen



if __name__ == "__main__":
   vorher=['toyimmg', 'iu', 'njyy', 'fldmlcl', 'xdt', 'oifv', 'a', 'zlbdicdy', 'idebqrfrow', 'uvb']
   alphabet="abcdefghijklmnopqrstuvwxyz"
   print vorher
   print mutation(vorher,alphabet)