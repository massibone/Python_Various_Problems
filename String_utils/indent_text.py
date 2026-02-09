def indent_text(text, spaces):
    """
    Aggiunge un numero specificato di spazi di indentazione a ogni riga del testo.
    
    Args:
        text (str): Il testo da indentare.
        spaces (int): Il numero di spazi da aggiungere all'inizio di ogni riga.
        
    Returns:
        str: Il testo indentato.
    """
    indentation = " " * spaces
    # splitlines(keepends=True) mantiene i caratteri di nuova riga originali
    lines = text.splitlines(keepends=True)
    return "".join(indentation + line for line in lines)
