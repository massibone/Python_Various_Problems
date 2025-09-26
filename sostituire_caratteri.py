'''
sostituisce - e spazio con spazio vuoto e infatti da 4111-1111-4555-1142 
restituisce
4111-1111-4555-1142 
'''
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

main()

pattern = '[a-z]t' # Modificato per cercare una lettera minuscola seguita da 't'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))
'''
// console output
['ot', 'st']
'''
#The caret, ^, placed at the beginning of the character class, matches all the characters except those specified in the class.
pattern = '[^a-z]t'
#// console output --> [' t']
Aggiunta tuple
constraints = [
            (nums, '[0-9]'),
            (lowercase, '[a-z]'),
            (uppercase, '[A-Z]'),
            (special_chars, '')

        ]
