import copy
import random

class Hat:
    def __init__(self, **kwargs):
        """
        Inizializza l'oggetto Hat e crea la lista 'contents'.

        :param kwargs: Coppie colore=numero, es. red=5, blue=2
        """
        # contents sarà una lista di stringhe, dove ogni stringa è il nome del colore
        self.contents = []

        # Itera sugli argomenti con parola chiave (kwargs)
        for color, count in kwargs.items():
            # Aggiunge il nome del colore alla lista 'contents' un numero di volte
            # pari al conteggio specificato
            self.contents.extend([color] * count)
    def draw(self, num_balls):
        """
        Estrae un numero specificato di palline a caso dal cappello SENZA reinserimento.
        
        :param num_balls: Il numero di palline da estrarre.
        :return: Una lista di stringhe che rappresentano le palline estratte.
        """
        # Se il numero di palline da estrarre supera la quantità disponibile, estrae tutte le palline.
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
            return drawn_balls
        
        # Estrae casualmente gli elementi senza reinserimento
        drawn_balls = random.sample(self.contents, num_balls)
        
        # Rimuove le palline estratte dalla lista contents
        for ball in drawn_balls:
            self.contents.remove(ball)
            
        return drawn_balls

    def __str__(self):
        """Rappresentazione leggibile per la stampa."""
        return f"Hat contents: {self.contents}"


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Esegue un esperimento Monte Carlo per stimare la probabilità di estrarre
    un certo gruppo di palline.
    
    :param hat: L'oggetto Hat originale (verrà copiato per ogni esperimento).
    :param expected_balls: Dizionario {colore: conteggio} atteso.
    :param num_balls_drawn: Numero di palline da estrarre per esperimento.
    :param num_experiments: Numero totale di esperimenti da eseguire.
    :return: La probabilità stimata (M/N).
    """
    successful_experiments = 0

    # 1. Funzione di supporto per verificare se l'estrazione soddisfa le aspettative
    def check_expectation(drawn, expected):
        # Converti la lista di palline estratte in un dizionario di conteggi
        drawn_counts = {}
        for color in drawn:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1
        
        # Verifica se tutti i colori attesi sono presenti nel conteggio richiesto
        for color, count in expected.items():
            if drawn_counts.get(color, 0) < count:
                return False
        return True

    # Esegui la simulazione
    for _ in range(num_experiments):
        # Crea una copia del cappello per ogni esperimento (senza modificare l'originale)
        # Importante: fare una copia profonda della lista contents
        hat_copy = Hat()
        hat_copy.contents = list(hat.contents) 

        # Esegui l'estrazione
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Verifica il successo
        if check_expectation(drawn, expected_balls):
            successful_experiments += 1

    # Restituisce la probabilità stimata
    return successful_experiments / num_experiments

# --- Esempio di Utilizzo e Test ---

if __name__ == "__main__":
    # Esempio fornito: 6 nere, 4 rosse, 3 verdi. Tentativo: 2 rosse, 1 verde, estraendo 5 palline, 2000 esperimenti.
    
    # Crea il cappello originale (la funzione experiment ne farà una copia)
    hat_original = Hat(black=6, red=4, green=3)

    probability = experiment(
        hat=hat_original,
        expected_balls={'red':2,'green':1},
        num_balls_drawn=5,
        num_experiments=2000
    )

    print(f"Probabilità stimata: {probability}")
    
    # Esempio 2 (più semplice): Probabilità di estrarre 1 verde su 1, da 1 verde e 1 blu, in 10000 esperimenti
    hat_simple = Hat(green=1, blue=1)
    probability_simple = experiment(
        hat=hat_simple,
        expected_balls={'green':1},
        num_balls_drawn=1,
        num_experiments=10000
    )
    # La probabilità matematica è 1/2 = 0.5
    print(f"\nProbabilità stimata (Hat verde=1, blu=1, estrai 1 verde): {probability_simple}")

'''
OUTPUT:
Probabilità stimata: 0.377

Probabilità stimata (Hat verde=1, blu=1, estrai 1 verde): 0.4972
'''
