# METHOD 1 : Using string slicing
def reverseNum(num):
    return int(str(num)[::-1])

# METHOD 2 : Using loop
def reverseNum(num):
    rev = 0
    while(num):
        rem = num%10
        rev = rev*10 + rem
        num = num // 10
    return rev

# METHOD 3 : Using Recursion
def reverseNum(num,rev=0):
    if(num==0):
        return rev
    return reverseNum(num//10,rev*10+num%10)

# But all these method are not able to revrse the trailing zero (1230) != 321
def reverseNum1(num):
    return str(num)[::-1]
print(reverseNum(1230)) #321
print(reverseNum1(1230)) # 0321