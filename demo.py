def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
arr=[22,100,45,200,88,4,8,10,15,20,44]
print (arr)
print(bubble_sort(arr))