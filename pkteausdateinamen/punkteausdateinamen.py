"""
Es werden Dateinamen aus dem Ordner ausgelesen und aus allen werden die Punkte bis 
auf den Punkt vor der Dateiendung entfernt.

http://www.programmieraufgaben.ch/aufgabe/punkte-aus-dateinamen-entfernen/cxrshndx

STATUS: laeuft aber quick and dirty

"""
import os

def entfernen(liste):
    zeichenliste=list(liste)
    pktezaehler=0
    for i in range(len(zeichenliste)):
        if zeichenliste[-i-1] == "." and pktezaehler:
            zeichenliste[-i-1] = ""
        elif zeichenliste[-i-1] == ".": 
            pktezaehler=1
    outstring=""
    for el in zeichenliste:
        outstring=outstring + str(el)
    return outstring

def einlesen():
    dateinamen=os.popen("ls").readlines()
    for i in range(len(dateinamen)):
        dateinamen[i]=dateinamen[i].rstrip()
    return dateinamen

def umbenennen():
    temp=einlesen()
    for index in range(len(temp)):
        os.system("mv {0} {1}".format(temp[index], entfernen(temp[index])))

if __name__ == "__main__":
    umbenennen()