#Calcolo costo di gestione di un'auto nuova per i primi 5 anni di vita

costoAcquisto = float(input("Inserire il prezzo di acquisto dell'auto nuova = "))
kmAnno = float(input("Km percorsi all'anno = "))
costoCarburante = float(input("Costo del carburante al litro/Kw = "))
efficenza = float(input("Rendimento del motore in km percorsi per litro/kW = "))
svalutazione = float(input("Valore dell'auto dopo 5 anni dall'acquisto = "))


costoTotCarburanteAnno = (kmAnno/efficenza)*costoCarburante
costoTotale = costoTotCarburanteAnno*5 + (costoAcquisto - svalutazione)
print("Nei 5 anni di possesso l'auto è costata = ",round(costoTotale,2))

