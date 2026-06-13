# push max to end

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[13,46,24,52,9,20]
print(bubble_sort(arr))
