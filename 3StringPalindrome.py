# METHOD 1 : Using string slicing
def is_Palindrome(s):
    return s == s[::-1]

# METHOD 2 : Using a loop
def is_Palindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

# METHOD 3 : Using reversed and join
def is_Palindrome(s):
    return s == "".join(reversed(s))

print(is_Palindrome("level"))