class Category:
    def __init__(self, name):
        self.name = name      # contiene il nome (es. "Food")
        self.ledger = []  # lista che riempiremo con oggetti tipo {'amount': 100, 'description': 'deposit'}
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total >= amount  # Restituisce True o False direttamente
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance 

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def __str__(self):
        # 1. Linea del Titolo
        # Nome centrato tra 30 asterischi (es. '*************Food*************')
        title = f"{self.name:*^30}\n"
        
        # 2. Corpo del Ledger
        items_string = ""
        for item in self.ledger:
            description = item['description']
            amount = item['amount']
            
            # Formattazione della descrizione: max 23 caratteri
            desc_formatted = description[:23].ljust(23)
            
            # Formattazione dell'importo: max 7 caratteri, 2 decimali, allineato a destra
            # Il formato '.2f' assicura 2 decimali. Riempiamo a 7 caratteri.
            amount_formatted = f"{amount:.2f}".rjust(7)
            
            # Composizione della riga e aggiunta a items_string
            items_string += f"{desc_formatted}{amount_formatted}\n"

        # 3. Linea del Totale
        total_line = f"Total: {self.get_balance():.2f}"
        
        return title + items_string + total_line

def create_spend_chart(categories):
    # 1. Calcolo Spese e Percentuali (Lasciato intatto, è corretto)
    category_spending = {}
    total_spending = 0
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        
        category_spending[category.name] = spent
        total_spending += spent

    if total_spending == 0:
        return "Percentage spent by category\n\nNon ci sono state spese."

    spent_percentages = {}
    for name, spent in category_spending.items():
        percent = (spent / total_spending) * 100
        # Arrotonda per difetto al 10 inferiore
        rounded_percent = int(percent // 10) * 10 
        spent_percentages[name] = rounded_percent

    # 2. Costruzione del Grafico

    chart_string = "Percentage spent by category\n"
    
    # Costruzione delle righe dell'asse y (100 | ... 0 |)
    for i in range(100, -1, -10):
        # Etichetta dell'asse y (es. "100| " o " 10| ")
        line = str(i).rjust(3) + "|"
        
        # Barre 'o'
        for category in categories:
            percent = spent_percentages[category.name]
            if percent >= i:
                line += " o "
            else:
                line += "   "
        
        chart_string += line + " \n" # Spazio finale (necessario per allineamento) + newline

    # 3. Linea orizzontale
    # Estensione corretta: 4 spazi per l'etichetta Y + 3 trattini per categoria + 1 trattino extra
    dash_line = "    " + ("---" * len(categories)) + "-\n"
    chart_string += dash_line
    
    # 4. Nomi delle categorie verticali (SEZIONE CORRETTA)
    
    max_name_length = max(len(cat.name) for cat in categories)
    
    for i in range(max_name_length):
        # Inizia con i 5 spazi di indentazione corretti (3 per etichetta + 1 per | + 1 per spazio)
        name_line = "     " 
        
        for category in categories:
            name = category.name
            
            # Se la categoria ha una lettera per questa riga (indice i)
            if i < len(name):
                # Aggiunge la lettera seguita da DUE spazi
                name_line += f"{name[i]}  " 
            else:
                # Altrimenti aggiunge TRE spazi vuoti
                name_line += "   " 
        
        # Dopo l'ultima categoria, la riga ha già i DUE spazi finali richiesti (grazie al ciclo)
        
        # Rimuove l'eventuale newline aggiuntiva solo se è l'ultima riga di tutte
        if i < max_name_length - 1:
            chart_string += name_line + "\n"
        else:
            # L'ultima riga non deve avere la newline
            chart_string += name_line

    return chart_string
