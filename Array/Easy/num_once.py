def num_once(arr):
    xor=0
    for num in arr:
        xor ^=num
    return xor

arr=[4,1,2,1,2]
arr1=[2,2,1]
print(num_once(arr1))