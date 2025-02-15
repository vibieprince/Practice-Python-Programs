def searchMany(list,x,k):
    count = 0
    for i in range(len(list)):
        if list[i] == x:
            count += 1
    if(count <= k):
        return True
    else:
        return False

print(searchMany([10, 17, 15, 12], 15, 1)) # returns True
print(searchMany([10, 12, 12, 12], 12, 2)) # returns False
print(searchMany([10, 12, 15, 11], 17, 18)) # returns True