'''
Reverse the order of the digits in the last four digits of card_number, by using a slice with a step of -1. 
You can use either negative or positive indices for the start and end indices. 
da 4111111145551142 per avere 2411
'''
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[-1:-5:-1]
    print(card_number_reversed)

'''
Per avere il reverse dal fondo all'inizio
card_number_reversed = card_number[::-1]
2411555411111114
'''
