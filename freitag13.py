"""
Bestimmung der Tage in einem gegebenen Datumsintervall
die auf Freitag, den 13. fallen

http://www.programmieraufgaben.ch/aufgabe/freitag-der-13-2/qju5xpiy

"""
import datetime as d

def freitag(date1,date2):
    temp=[]
    tempDay=date1
    delta=(date2 - date1).days
    if delta < 0:
        print "Das spaete Datum ist vor dem fruehen!"
    for i in range(delta):
        if tempDay.day==13 and tempDay.weekday()==4:
            temp.append(tempDay.isoformat())            
        tempDay=tempDay + d.timedelta(days=1)
    return temp

erstesDatum=d.date(1597,1,1) 
zweitesDatum=d.date(1600,12,31)

if freitag(erstesDatum , zweitesDatum) == []:
    print "Es liegen keine schwarzen Freitage zwischen " + erstesDatum.isoformat() + " und " +  zweitesDatum.isoformat()
else:
    print "Zwischen " + erstesDatum.isoformat() + " und " + zweitesDatum.isoformat() + "liegen folgende schwarze Freitage "
    print freitag(erstesDatum , zweitesDatum)