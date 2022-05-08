#Nome di file: creazione di un path assoluto

drive = input("Inserisci la lettera del volume = ")
root = input("Inserisci il percorso delle cartelle = ")
file = input("Inserisci il nome del file = ")
estensione = input("Inserisci l'estensione del file = ")

print("Il percorso assoluto è")
print(drive+":/"+root+file+"."+estensione)