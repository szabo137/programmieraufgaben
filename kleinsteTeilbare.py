"""
Bestimmung der kleinsten positiven natuerlichen Zahl, die durch alle Zahlen
von 1 bis n mit n natuelrlich teilbar ist.

http://www.programmieraufgaben.ch/aufgabe/kleinste-durch-zahlenreihe-von-1-bis-10-teilbare-zahl/047jo2x5

"""

def teilbar(zahl,teilers):
    # pruefe ob I:zahl durch alle zahlen bis I:teilers teilbar ist
    for el in range(teilers):
        if float(zahl) % float(el+1)==0:
            pruef=1
        else:
            return 0
    return pruef
            


def kleinsteTeilbare(zahl):
    temp=2.0
    while teilbar(temp,zahl)!=1:
        temp+=1
        print temp
    return int(temp)




n=10

print "die kleinste Zahl, die durch die Zahlen von 1 bis " + str(n) + " teilbar ist, lautet: " + str(kleinsteTeilbare(n))


"""
moegliche Verbesserung:

sei temp durch alle zahlen bis teilers teilbar, dann treten folgende faelle auf:

i)      teilers + 1 ist prim, dann ist temp*(teilers + 1) durch alle bis teilers+1 teilbar

ii)     teilers+1 ist potenz einer primzahl, also teilers+1=p**n mit einem natuerlichem n und p prim,
        dann ist temp*p durch alle bis teilers+1 teilbar

iii)    temp ist durch alle bis teilers+1 teilbar

mit diesem Verfahren kann man viele zu pruefenen Stellen ueberspringen und somit den Code erheblich beschleunigen



"""
