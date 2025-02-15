def count(s):
    vowels = 'AEIOUaeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count("I love India")) # 6