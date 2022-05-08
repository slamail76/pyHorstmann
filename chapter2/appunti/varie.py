#Calcolare tempo di spostamento
#Dati noti
import numpy as np
import datetime as dt
l1 = 6
dx = 10
dy = 3
s1 = 5 #espresso in Km/h
s2 = 2 #espresso in Km/h

# Ora effettuiamo un po di calcoli
t1 = 6 / 5
t1td = dt.timedelta(hours=t1)
t1dt = dt.datetime.min + t1td
print("{:%H:%M}".format(t1dt)) #Tempo impiegato per il primo percorso

l2 = np.sqrt(((dx-l1) ** 2) + (dy ** 2)) #Calcolo secondo segmento
t2 = l2 / s2
t2td = dt.timedelta(hours=t2)
t2dt = dt.datetime.min + t2td
print("{:%H:%M}".format(t2dt)) #Tempo impiegato per il primo percorso

tot = t1+ t2
tottd = dt.timedelta(hours=tot)
totdt = dt.datetime.min + tottd
print("Tempo totale impiegato per l'intero percorso {:%H:%M}".format(totdt))


