

from typing import Union
import math


# ============================================================================
# Classe Base: Vettore 2D (R²)
# ============================================================================

class R2Vector:
    """
    Rappresenta un vettore in uno spazio bidimensionale (R²).
    
    Attributes:
        x (float): Coordinata x del vettore
        y (float): Coordinata y del vettore
    
    Examples:
        >>> v = R2Vector(x=3, y=4)
        >>> print(v)
        (3, 4)
        >>> v.norm()
        5.0
    """
    
    def __init__(self, *, x: float, y: float):
        """
        Inizializza un vettore 2D.
        
        Args:
            x: Componente x del vettore
            y: Componente y del vettore
        
        Note:
            I parametri devono essere passati come keyword arguments.
        """
        self.x = x
        self.y = y

    def norm(self) -> float:
        """
        Calcola la norma (lunghezza) del vettore.
        
        La norma è calcolata come: |v| = √(x² + y²)
        
        Returns:
            float: La lunghezza del vettore
        
        Examples:
            >>> v = R2Vector(x=3, y=4)
            >>> v.norm()
            5.0
        """
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self) -> str:
        """
        Rappresentazione stringa user-friendly del vettore.
        
        Returns:
            str: Vettore in formato tupla (x, y)
        """
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self) -> str:
        """
        Rappresentazione ufficiale del vettore (per debugging).
        
        Returns:
            str: Rappresentazione che permette di ricreare l'oggetto
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other: 'R2Vector') -> 'R2Vector':
        """
        Somma tra due vettori.
        
        Args:
            other: Vettore da sommare
        
        Returns:
            R2Vector: Nuovo vettore risultato della somma
        
        Examples:
            >>> v1 = R2Vector(x=1, y=2)
            >>> v2 = R2Vector(x=3, y=4)
            >>> v3 = v1 + v2
            >>> print(v3)
            (4, 6)
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other: 'R2Vector') -> 'R2Vector':
        """
        Sottrazione tra due vettori.
        
        Args:
            other: Vettore da sottrarre
        
        Returns:
            R2Vector: Nuovo vettore risultato della sottrazione
        
        Examples:
            >>> v1 = R2Vector(x=5, y=7)
            >>> v2 = R2Vector(x=2, y=3)
            >>> v3 = v1 - v2
            >>> print(v3)
            (3, 4)
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other: Union['R2Vector', int, float]) -> Union['R2Vector', float]:
        """
        Moltiplicazione del vettore.
        
        Supporta due tipi di moltiplicazione:
        1. Scalare: v * k (moltiplica ogni componente per k)
        2. Prodotto scalare: v1 * v2 (dot product)
        
        Args:
            other: Scalare (int/float) o altro vettore
        
        Returns:
            R2Vector o float: Nuovo vettore (scalare) o numero (dot product)
        
        Examples:
            >>> v = R2Vector(x=2, y=3)
            >>> v2 = v * 2  # Moltiplicazione scalare
            >>> print(v2)
            (4, 6)
            
            >>> v1 = R2Vector(x=1, y=2)
            >>> v2 = R2Vector(x=3, y=4)
            >>> dot = v1 * v2  # Prodotto scalare
            >>> print(dot)
            11
        """
        if type(other) in (int, float):
            # Moltiplicazione per scalare
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            # Prodotto scalare (dot product)
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other: 'R2Vector') -> bool:
        """
        Verifica uguaglianza tra due vettori.
        
        Args:
            other: Vettore da confrontare
        
        Returns:
            bool: True se i vettori sono uguali
        """
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other: 'R2Vector') -> bool:
        """Verifica disuguaglianza tra due vettori."""
        return not self == other

    def __lt__(self, other: 'R2Vector') -> bool:
        """
        Confronto 'minore di' basato sulla norma.
        
        Un vettore è minore se ha norma inferiore.
        """
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other: 'R2Vector') -> bool:
        """Confronto 'maggiore di' basato sulla norma."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other: 'R2Vector') -> bool:
        """Confronto 'minore o uguale' basato sulla norma."""
        return not self > other

    def __ge__(self, other: 'R2Vector') -> bool:
        """Confronto 'maggiore o uguale' basato sulla norma."""
        return not self < other


# ============================================================================
# Classe Estesa: Vettore 3D (R³)
# ============================================================================

class R3Vector(R2Vector):
    """
    Rappresenta un vettore in uno spazio tridimensionale (R³).
    
    Estende R2Vector aggiungendo la componente z e il prodotto vettoriale.
    
    Attributes:
        x (float): Coordinata x del vettore
        y (float): Coordinata y del vettore
        z (float): Coordinata z del vettore
    
    Examples:
        >>> v = R3Vector(x=1, y=2, z=3)
        >>> print(v)
        (1, 2, 3)
        >>> v.norm()
        3.7416573867739413
    """
    
    def __init__(self, *, x: float, y: float, z: float):
        """
        Inizializza un vettore 3D.
        
        Args:
            x: Componente x del vettore
            y: Componente y del vettore
            z: Componente z del vettore
        """
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other: 'R3Vector') -> 'R3Vector':
        """
        Calcola il prodotto vettoriale (cross product) tra due vettori 3D.
        
        Il prodotto vettoriale v₁ × v₂ produce un nuovo vettore perpendicolare
        sia a v₁ che a v₂.
        
        Formula:
            (x₁, y₁, z₁) × (x₂, y₂, z₂) = 
            (y₁z₂ - z₁y₂, z₁x₂ - x₁z₂, x₁y₂ - y₁x₂)
        
        Args:
            other: Vettore 3D con cui calcolare il prodotto vettoriale
        
        Returns:
            R3Vector: Nuovo vettore perpendicolare a entrambi
        
        Examples:
            >>> v1 = R3Vector(x=1, y=0, z=0)
            >>> v2 = R3Vector(x=0, y=1, z=0)
            >>> v3 = v1.cross(v2)
            >>> print(v3)
            (0, 0, 1)
        
        Note:
            Il prodotto vettoriale non è commutativo: v₁ × v₂ ≠ v₂ × v₁
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)


# ============================================================================
# Funzioni Utility
# ============================================================================

def angle_between(v1: Union[R2Vector, R3Vector], 
                  v2: Union[R2Vector, R3Vector]) -> float:
    """
    Calcola l'angolo tra due vettori in radianti.
    
    Formula: cos(θ) = (v₁ · v₂) / (|v₁| × |v₂|)
    
    Args:
        v1: Primo vettore
        v2: Secondo vettore
    
    Returns:
        float: Angolo in radianti (0 a π)
    
    Examples:
        >>> v1 = R2Vector(x=1, y=0)
        >>> v2 = R2Vector(x=0, y=1)
        >>> angle = angle_between(v1, v2)
        >>> print(f"{math.degrees(angle):.1f}°")
        90.0°
    """
    if type(v1) != type(v2):
        raise TypeError("I vettori devono essere dello stesso tipo")
    
    dot_product = v1 * v2
    magnitude_product = v1.norm() * v2.norm()
    
    if magnitude_product == 0:
        raise ValueError("Impossibile calcolare l'angolo con vettore nullo")
    
    cos_angle = dot_product / magnitude_product
    # Clamp per evitare errori di arrotondamento
    cos_angle = max(-1, min(1, cos_angle))
    
    return math.acos(cos_angle)


def are_orthogonal(v1: Union[R2Vector, R3Vector], 
                   v2: Union[R2Vector, R3Vector], 
                   tolerance: float = 1e-10) -> bool:
    """
    Verifica se due vettori sono ortogonali (perpendicolari).
    
    Due vettori sono ortogonali se il loro prodotto scalare è zero.
    
    Args:
        v1: Primo vettore
        v2: Secondo vettore
        tolerance: Tolleranza per errori di arrotondamento
    
    Returns:
        bool: True se i vettori sono ortogonali
    
    Examples:
        >>> v1 = R2Vector(x=1, y=0)
        >>> v2 = R2Vector(x=0, y=1)
        >>> are_orthogonal(v1, v2)
        True
    """
    return abs(v1 * v2) < tolerance


def are_parallel(v1: Union[R2Vector, R3Vector], 
                 v2: Union[R2Vector, R3Vector],
                 tolerance: float = 1e-10) -> bool:
    """
    Verifica se due vettori sono paralleli.
    
    Due vettori sono paralleli se uno è un multiplo scalare dell'altro.
    
    Args:
        v1: Primo vettore
        v2: Secondo vettore
        tolerance: Tolleranza per errori di arrotondamento
    
    Returns:
        bool: True se i vettori sono paralleli
    
    Examples:
        >>> v1 = R2Vector(x=2, y=4)
        >>> v2 = R2Vector(x=1, y=2)
        >>> are_parallel(v1, v2)
        True
    """
    if type(v1) != type(v2):
        return False
    
    # Calcola il prodotto vettoriale (per R3) o verifica il rapporto (per R2)
    if isinstance(v1, R3Vector):
        cross = v1.cross(v2)
        return cross.norm() < tolerance
    else:
        # Per R2, verifica se x₁/x₂ = y₁/y₂
        try:
            ratio_x = v1.x / v2.x if v2.x != 0 else float('inf')
            ratio_y = v1.y / v2.y if v2.y != 0 else float('inf')
            return abs(ratio_x - ratio_y) < tolerance
        except ZeroDivisionError:
            return False


# ============================================================================
# Esempi e Demo
# ============================================================================

def run_examples():
    """Esegue esempi dimostrativi della libreria"""
    
    print("=" * 70)
    print("VECTOR MATH LIBRARY - Esempi d'Uso")
    print("=" * 70)
    
    # Esempio 1: Vettori 2D
    print("\n📐 ESEMPIO 1: Vettori 2D (R²)")
    print("-" * 70)
    v1 = R2Vector(x=3, y=4)
    v2 = R2Vector(x=1, y=2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 · v2 (dot product) = {v1 * v2}")
    print(f"|v1| (norma) = {v1.norm():.2f}")
    print(f"v1 == v2? {v1 == v2}")
    print(f"v1 > v2? {v1 > v2}")
    
    # Esempio 2: Vettori 3D
    print("\n🎲 ESEMPIO 2: Vettori 3D (R³)")
    print("-" * 70)
    v3 = R3Vector(x=2, y=3, z=1)
    v4 = R3Vector(x=0.5, y=1.25, z=2)
    
    print(f"v3 = {v3}")
    print(f"v4 = {v4}")
    print(f"v3 + v4 = {v3 + v4}")
    print(f"v3 - v4 = {v3 - v4}")
    print(f"v3 · v4 (dot product) = {v3 * v4:.2f}")
    print(f"v3 × v4 (cross product) = {v3.cross(v4)}")
    print(f"|v3| (norma) = {v3.norm():.2f}")
    
    # Esempio 3: Funzioni utility
    print("\n🔧 ESEMPIO 3: Funzioni Utility")
    print("-" * 70)
    va = R2Vector(x=1, y=0)
    vb = R2Vector(x=0, y=1)
    
    angle = angle_between(va, vb)
    print(f"v_a = {va}")
    print(f"v_b = {vb}")
    print(f"Angolo tra v_a e v_b = {math.degrees(angle):.1f}°")
    print(f"Sono ortogonali? {are_orthogonal(va, vb)}")
    print(f"Sono paralleli? {are_parallel(va, vb)}")
    
    vc = R2Vector(x=2, y=4)
    vd = R2Vector(x=1, y=2)
    print(f"\nv_c = {vc}")
    print(f"v_d = {vd}")
    print(f"Sono paralleli? {are_parallel(vc, vd)}")
    
    print("\n" + "=" * 70)
    print("✅ Esempi completati!")
    print("=" * 70)


if __name__ == '__main__':
    # Esegui gli esempi quando il file viene lanciato direttamente
    run_examples()
