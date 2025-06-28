'''
Crea documento LaTeX con un semplice contenuto di esempio e lo salverà come "documento_latex.tex" nella directory corrente. 
Quindi, utilizzerà il comando pdflatex per compilare il file .tex in un documento PDF. 
Infine, stampa un messaggio per confermare che il documento è stato generato correttamente. 
'''
# Importiamo il modulo os per gestire i file
import os

# Definiamo il contenuto del documento LaTeX
latex_content = """
\\documentclass{article}
\\begin{document}
\\section*{Esempio di documento LaTeX generato con Python}


Questo è un esempio di come è possibile generare un documento LaTeX utilizzando Python.

\\begin{itemize}
\\item Puoi creare elenchi puntati
\\item Inserire formule matematiche: $E=mc^2$
\\item Aggiungere tabelle e molto altro ancora!
\\end{itemize}

\\end{document}
"""

# Definiamo il percorso del file .tex da creare
file_path = "documento_latex.tex"

# Apriamo il file in modalità scrittura e scriviamo il contenuto LaTeX
with open(file_path, "w") as file:
    file.write(latex_content)

# Compiliamo il file .tex in un documento PDF utilizzando il comando pdflatex
os.system(f"pdflatex {file_path}")

# Stampiamo un messaggio per confermare che il documento è stato generato
print(f"Il documento LaTeX è stato generato correttamente come {os.path.splitext(file_path)[0]}.pdf")
