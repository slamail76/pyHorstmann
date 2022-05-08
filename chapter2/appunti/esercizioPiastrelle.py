#calcolare il numero di piastrelle sapendo che la prima e l'ultima devono essere nere
#dichiariamo le costanti
LUNGEZZA_PIASTRELLA = 5
LUNGHEZZA_TOTALE = 100
LUNGHEZZA_COPPIE = LUNGEZZA_PIASTRELLA * 2
numeroCoppie = int((LUNGHEZZA_TOTALE - LUNGEZZA_PIASTRELLA) / LUNGHEZZA_COPPIE)
numero_piastrelle = numeroCoppie*2+1
spazio_laterale = (LUNGHEZZA_TOTALE - (numero_piastrelle*LUNGEZZA_PIASTRELLA)) / 2
print("Il numero di piastrelle usate è ",numero_piastrelle)
print("Lo spazio laterale tra piastrella e muro è ",spazio_laterale)
