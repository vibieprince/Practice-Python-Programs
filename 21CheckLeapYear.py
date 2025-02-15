def checkYear(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return True
    else:
        return False

print(checkYear(2028)) # True
print(checkYear(1900)) # False