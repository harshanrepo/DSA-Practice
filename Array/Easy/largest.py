def largest(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[2,5,1,3,0]
print(largest(arr))