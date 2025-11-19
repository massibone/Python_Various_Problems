class Rectangle:
   
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 2. Rappresentazione in stringa per la stampa (requisito: 'Rectangle(width=5, height=10)')
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
   
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # Utilizza self.width e self.height
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        # La formula usa il teorema di Pitagora
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # 5. Metodo get_picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        # Crea la stringa del rettangolo
        picture = ""
        # Cicla per l'altezza (numero di righe)
        for _ in range(self.height):
            # Aggiunge la riga di asterischi (larghezza) più il newline
            picture += "*" * self.width + "\n"
        return picture

    # 6. Metodo get_amount_inside
    def get_amount_inside(self, other):
        # Controlla se l'oggetto passato è una forma valida (Rectangle o Square)
        if not isinstance(other, (Rectangle, Square)):
            raise TypeError("L'oggetto passato deve essere una forma (Rectangle o Square).")
       
        # Calcola quante volte la larghezza 'other' entra nella larghezza 'self'
        fit_width = self.width // other.width
        # Calcola quante volte l'altezza 'other' entra nell'altezza 'self'
        fit_height = self.height // other.height
       
        # Il numero totale di forme è il prodotto
        return fit_width * fit_height


class Square(Rectangle):
    # 1. Costruttore: prende una sola dimensione 'side'
    def __init__(self, side):
        # Chiama il costruttore del genitore, passando 'side' sia per larghezza che per altezza
        super().__init__(side, side)

    # 2. Rappresentazione in stringa (requisito: 'Square(side=9)')
    def __str__(self):
        # Poiché width == height, possiamo usare self.width per ottenere il lato
        return f'Square(side={self.width})'

    # 3. Metodo aggiuntivo set_side
    def set_side(self, side):
        # Imposta sia larghezza che altezza
        self.width = side
        self.height = side

    # 4. Sovrascrittura dei metodi set_width e set_height
    #    (Per garantire che se uno cambia, anche l'altro cambi)
    def set_width(self, side):
        # Sovrascrive il metodo del genitore
        self.set_side(side)

    def set_height(self, side):
        # Sovrascrive il metodo del genitore
        self.set_side(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

