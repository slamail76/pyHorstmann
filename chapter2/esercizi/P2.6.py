#Convertitore metro pollici, piedi, miglia
MTPOLL = 39.37
MTPIED = 3.281
MTMIGL = 0.00062

misura = float(input("Inserisci una misura espressa in metri : "))
#Risultati
print(misura,"MT  corrispondono a\t",round((misura*MTPOLL),2), "\t\tpollici")
print(misura,"MT  corrispondono a\t",round((misura*MTPIED),2), "\t\tpiedi")
print(misura,"MT  corrispondono a\t",(misura*MTMIGL), "\tmiglia")
