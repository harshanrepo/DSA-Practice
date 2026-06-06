def subarray_k(arr,k):
    left=0
    max_lenght=0
    current_Sum=0
    for right in range(len(arr)):
        current_Sum+=arr[right]

        while current_Sum>k and left<=right:
            current_Sum-=arr[left]
            left+=1

        if current_Sum==k:
            max_lenght=max(max_lenght,right-left+1)
    return max_lenght

arr=[1, 2, 3, 1, 1, 1]
k=3
print(subarray_k(arr,k))