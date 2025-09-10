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

