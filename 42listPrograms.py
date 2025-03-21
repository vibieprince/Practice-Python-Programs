#Illustrate different list slicing constructs for the following operations on the
# following list:
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1. Return a list of numbers starting from the last to second item of the list
# 2. Return a list that start from 3rd item to second last item.
# 3. Return a list that has only even position elements of list L to list M.
# 4. Return a list that starts from the middle of the list L.
# 5. Return a list that reverses all the elements starting from element at index 0 to middle index only and return the entire list.
# 6. Divide each element of the list by 2 and replace it with the remainder


l = [1,2,3,4,5,6,7,8,9]

print(l[-1:0:-1]) #1

print(l[2:-1:]) #2

m = []

for i in l:
    if i%2==0:
        m.append(i)
    
print(m) #3

n = len(l)//2
print(l[n::]) #4

k = l[n::-1] + l[n+1:]
print(k) #5

l = [x%2 for x in l]

print(l)