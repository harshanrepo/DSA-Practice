'''def check_sort(arr):
    n=len(arr)
    if n<=1:
        return -1
    for i in range(n):
        if arr[i]<=arr[i+1]:
            return True
        return False
arr=[1,2,3,4,5]
arr1=[5,4,6,7,8]
print(check_sort(arr1))'''


# Leetcode - check sort and rotate.

def is_sorted(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            count +=1
    return count<=1

arr=[1,2,3,4,5]
arr1=[5,4,6,7,8]
print(is_sorted(arr))