# rovescia una stringa usando la ricorsione

def reverse_recursive(s: str) -> str:
    """
    Rovescia una stringa usando la ricorsione.
    Esempio:
        reverse_recursive("Python") -> "nohtyP"
    """
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

# Esempi d'uso
if __name__ == "__main__":
    sample = "Automazione"
    print(reverse_recursive(sample))  # Output: "enoizamotuA"
