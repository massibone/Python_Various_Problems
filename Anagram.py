str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

def anagram(str1,str2):
    l1=list(str1)
    l2=list(str2)
    if sorted(l1) == sorted(l2):
        print("yess Anagrams")
    else:
        print("noo not anagrams")



anagram(str1,str2)

'''
Enter the first word: modern
Enter the second word: norman
noo not anagrams
'''
