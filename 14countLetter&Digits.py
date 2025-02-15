def countLetterDigits(s):
    lcount = 0
    dcount = 0
    for i in s:
        if i.isalpha():
            lcount += 1
        if i.isdigit():
            dcount += 1
    with open("count.txt","w") as file:
        file.write(f"Number of letters : {lcount}\n")
        file.write(f"Number of digits : {dcount}")
    
countLetterDigits("Hel456 my253e 446ince5553gh")