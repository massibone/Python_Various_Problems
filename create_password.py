'''
Create a pwd of 8 chars
'''
import random
def pwd(length):
        pw=str()
        char="abCdeFghjkliIlMNOPpopnmqQRrstuxvzYXWw" + "1203456789*_"
        for i in range(length):
                pw=pw + random.choice(char)
        return pw
