"""
*******************
mutant.py
*******************

Es sollen 100 Zufallsworte generiert werden, aus welchen dann durch ein
Evolutionsprozess ein Zielwort entstehen soll.

http://www.programmieraufgaben.ch/aufgabe/mutanten/nwh8mrey

separate Module:
    zufallswort.py
    selektion.py
    crossover.py
    mutation.py

"""

#import random as r

def evolution(ersteGeneration, ziel,abc,selecGewicht=[1.0,1.0,1.0],mutaAnteil=0.1):
    neueGen=ersteGeneration
    laufIndex=0.0
    while True:
        tempSelec=selektion(neueGen,ziel,selecGewicht)
        tempGen=crossover(tempSelec,len(ersteGeneration))
        neueGen=mutation(tempGen,abc,mutaAnteil)
        laufIndex+=1
        print laufIndex
        if laufIndex > 1000000:
            print "Ueberlauf!!"
            break
        if neueGen[0]==ziel:
            return laufIndex



if __name__ == "__main__":


    from zufallswort import *

    from selektion import *

    from mutation import *

    from crossover import *


    # erste Generation erzeugen:
    anzahl=100
    maximalL=10
    alphabet="abcdefghijklmnopqrstuvwxyz"
    Gen=zufallswoerter(anzahl,maximalL,alphabet)
    ziel="tag"
    ende=evolution(Gen,ziel,alphabet)
    print "Das Ziel ist nach",int(ende) , "Schritten erreicht."
