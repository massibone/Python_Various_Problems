import datetime

def months(d1, d2):
    return d1.month - d2.month + 12*(d1.year - d2.year)

d1 = datetime.datetime(2017, 3, 14)
d2 = datetime.datetime(2023, 4, 30)

print(months(d1, d2))
