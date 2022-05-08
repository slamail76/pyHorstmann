#esempi su stringhe
name = "jerry"
print(name[1])
lunghezza = len(name)
print(lunghezza)
print(name.upper())
print(name.count("r"))
print(name.replace(name,"tom"))
print(chr(98))
#escape \
print('Il gatto e l\'uccello sono amici')
print("Un testo lungo a un certo punto va \n a capo")

flnumber = 1.37276484
print(f"Numero floating è {round(flnumber,2)}")  # f-String method

print("gatto"+" "+"cane")
print("gatto",4,"cane")