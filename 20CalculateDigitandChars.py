def calculate(s):
    digit = 0
    upper = 0
    lower = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
        if i.isdigit():
            digit += 1
    
    print(f"Number of digits : {digit}\nNumber of uppercase letters : {upper}\nNumber of lowercase letters : {lower}")

calculate("Hel456 mT253e 446INce5553gh")