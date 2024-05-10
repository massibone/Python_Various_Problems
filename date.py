date = input("Enter your date of birth in YYYYMMDD format: > ")
sum_list = []

def digitOfLife(date):
    sum = 0
    if(len(date) > 8):
        print("Input data too long")
        return
    else:
        date_list = []
        for char in date:
            date_list.append(int(char))
            
        for num in date_list:
            sum+=num
            if sum > 9:
                sum = sum%10 +sum//10
    return sum
    
print(digitOfLife(date))
'''
Enter your date of birth in YYYYMMDD format: > 199912296
Enter your date of birth in YYYYMMDD format: > 200001014
'''
