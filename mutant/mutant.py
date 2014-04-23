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

import random as r

from zufallswort import *

from selektion import *

from mutation import *

from crossover import *

if __name__ == "__main__":
    anzahl=10
    maximalL=6
    alphabet="abcdefghijklmnopqrstuvwxyz"

    print zufallswoerter(anzahl,maximalL,alphabet)
