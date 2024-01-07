import numpy as np
r = 3
perimetroCerchio = (r * 2) * np.pi
areaCerchio =  (r ** r) * np.pi
print(f"Il perimetro del cerchio è {perimetroCerchio} mm mentre l'area è {areaCerchio} mmq")
print("Testo con suono \u041b \n ciao")

prezzo = 35000
testo = "Il prezzo è di € {:+,.2f}".format(prezzo)
print(testo)