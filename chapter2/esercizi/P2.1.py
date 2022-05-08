"""Scrivere un programma che visualizzi le dimensioni in millimetri di un foglio
di carta in formato lettere (8.5 x 11 pollici, un pollice = 25.4 millimetri). Usate
le opportuni costanti e commentate adeguatamente"""
POLLICE = float(25.4) #Dichiarazione di costante per un pollice
latoC = float(input("Inserisci il lato corto del foglio :"))
latoL = float(input("Inserisci il lato lungo del foglio :"))
print("Dimensioni in millimetri del formato lettera è {} x {}".format(round(POLLICE*latoC,2),POLLICE*latoL))


