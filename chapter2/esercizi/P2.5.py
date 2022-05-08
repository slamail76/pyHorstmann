#Programma che effettua calcoli su due numeri inseriti dall'utente
#presentando l'output in una struttura tabulata

num1 = float(input("Inserisci il primo numero : "))
num2 = float(input("Inserisci il secondo numero : "))

# Calcoli
print("Sum:\t\t",num1+num2)
print("Difference:\t",num1-num2)
print("Product\t\t",num1*num2)
print("Average\t\t",(num1+num2)/2)
print("Distance\t",abs(num1-num2))
print("Maximum\t\t",max(num1,num2))
print("Minimum\t\t",min(num1,num2))