#Programma che chiede di inserire lunghezza del raggio e visualizza l'area e la circonferenza
#e superficie e volume di una sfera avente stesso raggio

import numpy as np
raggio = float(input("Inserisci il raggio = "))

#calcolo area e circonferenza del cerchio
areaCerchio = (raggio ** 2) + np.pi
circoCerchio = raggio * 2 * np.pi
# calcolo del volume di una sfera (4pi*r**3)/3
# calcolo dell'area di una sfera 4πr2
volumeSfera = ((4*np.pi)*raggio ** 3)/3
superficieSfera = (4*np.pi) * (raggio ** 2)

#Stampa risultati
print("L'area del cerchio con raggio ",raggio," è ",areaCerchio)
print("La circonferenza del cerchio con raggio ",raggio," è ",circoCerchio)
print("Il volume della sfera con raggio ",raggio," è ",volumeSfera)
print("La superficie della sfera con ",raggio," è ",superficieSfera)
