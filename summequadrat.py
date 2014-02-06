"""
Dies ist die Loesung der Aufabe "Summe Quadrat" auf

http://www.programmieraufgaben.ch/aufgabe/summe-quadrat/3vw2uxzp

"""



def quadrat(liste):
    temps=range(len(liste))
    for index in range(len(liste)):
        temps[index]=liste[index]**2
    return temps

def summe(listen):
    temp=0
    for el in listen:
        temp+=el
    return temp




u=range(11)  #bis 11, da u[0]=0



#erst quadrieren, dann summieren:

print "die Summe der Quadrate von 1 bis 10 ist: " + str(summe(quadrat(u)))

#erst summieren, dann quadrieren:

print "das Quadrat der Summe von 1 bis 10 ist: " + str(summe(u)**2)

#differenz:

print "die Differenz betraegst: " + str(summe(u)**2-summe(quadrat(u)))