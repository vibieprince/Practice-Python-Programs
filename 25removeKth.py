def removeKth(s,i):
    if(i<0 or i>=len(s)):
        return s
    return s[:i]+s[i+1:]

print(removeKth("hello",6)) # hello
print(removeKth("hello",-1)) # hello
print(removeKth("hello",3)) # helo