def factors(n):
    ans = []
    for i in range(1,n+1):
        if(n%i==0):
            ans.append(i)
    return ans

print(factors(12)) # [1, 2, 3, 4, 6, 12]