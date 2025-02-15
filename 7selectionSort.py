def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mindIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[mindIndex]:
                mindIndex = j
        
        arr[i], arr[mindIndex] = arr[mindIndex], arr[i]
    
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted Array : ",arr)