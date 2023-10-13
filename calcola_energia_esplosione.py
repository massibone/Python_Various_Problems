def calcola_energia_esplosione(massa_kg):
    velocita_luce = 3.00e8  # Velocità della luce in metri/secondo
    energia_joule = massa_kg * velocita_luce ** 2
    return energia_joule

if __name__ == "__main__":
    massa_esplosivo_kg = 1000  # Esempio di massa dell'esplosivo in kg
    energia_esplosione_joule = calcola_energia_esplosione(massa_esplosivo_kg)
    print(f"Energia liberata dall'esplosione: {energia_esplosione_joule} joule")
