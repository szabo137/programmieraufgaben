"""
*******************
mutant.py
*******************

Es sollen 100 Zufallsworte generiert werden, aus welchen dann durch ein 
Evolutionsprozess ein Zielwort entstehen soll.

http://www.programmieraufgaben.ch/aufgabe/mutanten/nwh8mrey

separate Module:
    zufallswort.py

"""

import random as r

def zufallswort(maxL,abc):
    L=r.randint(1,maxL)
    temp=""
    for index in range(L):
        temp=temp + str(abc[r.randint(0,len(abc)-1)])
    return temp

def zufallswoerter(anz,maxL,abc):
    temp=[]
    for i in range(anz):
        temp.append(zufallswort(maxL,abc))
    return temp




if __name__ == "__main__":
    anzahl=10
    maximalL=1
    alphabet="abcdefghijklmnopqrstuvwxyz"

    print zufallswoerter(anzahl,maximalL,alphabet)
