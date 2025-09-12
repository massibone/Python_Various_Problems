text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % 26
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

'''
Output
char: h encrypted text: k
char: e encrypted text: kh
char: l encrypted text: kho
char: l encrypted text: khoo
char: o encrypted text: khoor
char:   encrypted text: khoor 
char: z encrypted text: khoor c
char: a encrypted text: khoor cd
char: i encrypted text: khoor cdl
char: r encrypted text: khoor cdlu
char: a encrypted text: khoor cdlud

% 26 che è la lunghezza dell'alfabeto senno' ci sarebbe un raise error
posso sostituire %26 con len(alphabet)

'''
