# A website requires the users to input username and password to register. Construct
# a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12

import re

def isValidPass(password):
    if not (6<=len(password)<=12):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[$#@]',password):
        return False
    return True

password = input("Enter your password :")

if isValidPass(password):
    print("Passowrd is valid ✅")
else:
    print("Password is invalid ❌")