import numpy as np
POLLICE = 25.4 # mm per pollice
verticale = 11
orizzontale = 8.5

vert_mm = verticale * POLLICE
oriz_mm = orizzontale * POLLICE
perimetro = vert_mm * 2 + oriz_mm * 2

diagonale = np.sqrt((vert_mm ** 2) + (oriz_mm ** 2))

print("Il perimetro di un foglio A4 è di " + str(round((perimetro),2)) + " mm")
print("La diagonale di un foglio A4 è di " + str(round((diagonale),2)) + " mm")