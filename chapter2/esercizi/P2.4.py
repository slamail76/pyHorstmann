#Programma che effettua calcoli su due numeri inseriti dall'utente

num1 = float(input("Inserisci il primo numero : "))
num2 = float(input("Inserisci il secondo numero : "))

# Calcoli
print("La somma di ",num1, " e ", num2, "è ",num1+num2)
print("La differenza di ",num1, " e ", num2, "è ",num1-num2)
print("Il prodotto di ",num1, " e ", num2, "è ",num1*num2)
print("La media di ",num1, " e ", num2, "è ",(num1+num2)/2)
print("La distanza di ",num1, " e ", num2, "è ",abs(num1-num2))
print("Il valore massimo di ",num1, " e ", num2, "è ",max(num1,num2))
print("Il valore minimo di ",num1, " e ", num2, "è ",min(num1,num2))
