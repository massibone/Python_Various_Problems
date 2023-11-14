
'''
Metto 81 gettoni, ognuno con un 3 su un lato e un 4 sull'altro lato.Aggiungo 9 gettoni con un 3 da una parte e un 2 dall'altra.E infine aggiungo ancora un gettone con un 2 da una parte e 
l dall'altra. Méscolali. Tu estrarrai a caso un gettone dall'urna e, senza guardarlo, 
lo getterai in aria; poi guarderai il Iato rivolto verso l'alto e dovrai 
indovinare il numero che si trova dall'altra parte. Se indovini giusto, 
sei libero, se sbagli sarai messo a morte; ma puoi rifiutare d'indovinare; in questo caso resti in prigione, senza pericolo per la tua vita. 
'''
'''
Se hai un solo tiro e il lato sopra è "1", allora puoi essere certo che il lato opposto sarà "2". Nel caso in cui il lato sopra mostri un "2", ci sono due possibilità: il lato opposto potrebbe essere "1" o "3.Se il lato sopra è "3", allora ci sono due possibilità per il lato opposto: "4" o "2". La tua correzione è corretta: hai 81 gettoni con "3" e "4" sull'altro lato e 9 gettoni con "3" e "2" sull'altro lato.

Quindi, se il lato sopra è "3", devi fare una scelta tra "4" e "2". In questo caso, non puoi essere certo dell'altro numero, e la probabilità di indovinare correttamente dipende dalla distribuzione di "4" e "2" nei tuoi gettoni. Se hai una distribuzione uniforme, la probabilità di indovinare correttamente "4" o "2" è la stessa.
'''
import random

# Creazione degli gettoni nell'urna
gettoni = ["3-4"] * 81 + ["3-2"] * 9 + ["2-1"]

# Estrarre casualmente un gettone
gettone_estratto = random.choice(gettoni)

# Separare i lati del gettone
lato_sopra, lato_sotto = gettone_estratto.split("-")

# Stampa i risultati
print(f"Lato sopra: {lato_sopra}")
print(f"Lato sotto: {lato_sotto}")

# Se il lato sopra è "3", indovina il lato sotto
if lato_sopra == "3":
    indovinato = lato_sotto
    print(f"Indovinato: {indovinato}")
else:
    print("Non è possibile indovinare con certezza.")
