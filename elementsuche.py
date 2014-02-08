"""
Zu einem gegebenen Array und einer gegebenen Zahl, soll die Stelle ausgegeben werden
an der sich die Zahl im Array befindet.

http://www.programmieraufgaben.ch/aufgabe/suche-element-in-array-feld/t2hd0qw5

"""

a=[2, 17, 10, 9, 16, 3, 9, 16, 5, 1, 17, 14]

gesuchteZahl=int(input("Welche Zahl soll im Array gefunden werden? "))

try:
    print "Die gesuchte Zahl " + str(gesuchteZahl) + " befindet sich an der Stelle " +str(a.index(gesuchteZahl)+1) + " im Array."
except:
    print "Die gesuchte Zahl befindet sich nicht im Array"