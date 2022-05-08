# Programma che legge un numero in entrata e calcola il quadrato, il cubo, e IV potenza

number = float(input("Inserisci un numero :"))
quadrato = number ** 2
cubo = number ** 3
quarta = number ** 4
# Visualizzazione
print("Il quadrato di %.2f" % number + " is " + str(quadrato))
print("Il cubo di %.2f" % number + " is " + str(cubo))
print("La quarta potenza di %.2f" % number + " is " + str(quarta ))