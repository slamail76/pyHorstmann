#Programma che calcola lìarea e il perimetro del rettangolo e la sua diagonale
import numpy as np

lato1 = float(input("Inserisci il primo lato : "))
lato2 = float(input("Inserisci il secondo lato : "))

#Calcoli
area = lato1*lato2
perimetro = lato1*2 + lato2*2
diagonale = np.sqrt((lato1**2) + (lato2 ** 2))

#stampa
print("L'area del rettangolo è = ",area)
print("Il perimetro del rettangolo è = ",perimetro)
print("La diagonale del rettangolo è = ",diagonale)

