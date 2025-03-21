def retSmaller(lists):
    if not lists:
        return None
    
    smallerList = lists[0]
    for sublist in lists[1:]:
        if len(sublist) < len(smallerList):
            smallerList = sublist
        
    return smallerList


print(retSmaller([ [ -2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6 , 7, 8, 9, 10], [11, 12, 13, 14, 15]]))

print(retSmaller([[-2, -1, 0, 0.12, 1, 2], ['a', 'b', 'c', 'd', 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))