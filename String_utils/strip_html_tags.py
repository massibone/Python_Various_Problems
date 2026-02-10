import re

def strip_html_tags(text):
    """
    Rimuove i tag HTML semplici da una stringa.
    
    Args:
        text (str): La stringa contenente tag HTML.
        
    Returns:
        str: La stringa senza tag HTML.
    """
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)

# Test della funzione
if __name__ == "__main__":
    test_html = "<p>Hello <b>World</b></p>"
    result_html = strip_html_tags(test_html)

    print("Testo HTML originale:")
    print(test_html)
    print("\nTesto senza tag HTML:")
    print(result_html)

    expected_html = "Hello World"
    assert result_html == expected_html
    print("\nTest strip_html_tags superato con successo!")

    test_html_complex = "<div><p>This is a <span>test</span> with <a href=\"#\">multiple</a> tags.</p></div>"
    result_html_complex = strip_html_tags(test_html_complex)
    print("\nTesto HTML complesso originale:")
    print(test_html_complex)
    print("\nTesto complesso senza tag HTML:")
    print(result_html_complex)
    expected_html_complex = "This is a test with multiple tags."
    assert result_html_complex == expected_html_complex
    print("\nTest strip_html_tags complesso superato con successo!")

