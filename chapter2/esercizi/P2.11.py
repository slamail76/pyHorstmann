#Programma che calcola il costo per percorrere 100 Km e quantità rimasta di carburante

quantityFuel = float(input("Quantità di carburante nel serbatoio = "))
efficienza = float(input("Quanti Km fai con un litro di benzina ? = "))
costoBenzina = float(input("Quando costa la benzina al litro ? = "))

#Calcoli
consumoBenzina = 100 / efficienza
residuoSerbatoio = quantityFuel - consumoBenzina
costo100Km = consumoBenzina * costoBenzina

print("Per percorrere 100 Km sono necessari ",costo100Km, "€")
print("Dopo aver percorso 100Km rimangono nel serbatoio ",residuoSerbatoio, " litri")