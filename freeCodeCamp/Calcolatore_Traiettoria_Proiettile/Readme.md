Calcolatore di Traiettoria Proiettile

Questo progetto implementa una simulazione della traiettoria di un proiettile, tenendo conto della velocità iniziale, dell'altezza e dell'angolo di lancio, in un ambiente con accelerazione gravitazionale costante. L'output include un grafico a caratteri (ASCII art) che visualizza la parabola del proiettile.
Struttura del Codice
Il progetto è interamente contenuto nel file projectile_class.py e si basa su due classi principali:
Projectile: Gestisce i calcoli fisici, la scomposizione vettoriale e la determinazione delle coordinate $x$ e $y$ in un dato momento.
Graph: Si occupa della visualizzazione, convertendo le coordinate float calcolate in un grafico 2D discreto con assi $X$ e $Y$.
Requisiti
Il progetto richiede solo l'installazione di Python 3 (versione 3.6 o successiva).
Non sono richieste librerie esterne oltre a math, che è standard di Python.
Esecuzione
Per eseguire la simulazione con i parametri predefiniti (Velocità: 10 m/s, Altezza: 3 m, Angolo: 45°):
Salva il codice nel file projectile_class.py.
Esegui lo script dal terminale:
python projectile_class.py

Output di Esempio
L'output mostrerà prima i dettagli fisici del lancio e il dislocamento totale, seguito dal grafico della traiettoria:
Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 12.6 m

⊣     ∙       
⊣  ∙∙∙ ∙∙∙    
⊣ ∙       ∙   
⊣∙         ∙  
⊣           ∙ 
⊣            ∙
⊣             
 TTTTTTTTTTTTT

Come Modificare i Parametri
Puoi facilmente modificare i parametri di simulazione nel blocco di codice finale all'interno di if __name__ == "__main__": in projectile_class.py:
if __name__ == "__main__":
    # Modifica qui:
    ball = Projectile(20, 5, 60) # Esempio: 20 m/s, Altezza 5 m, Angolo 60°
    print(ball)
    
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_trajectory())


