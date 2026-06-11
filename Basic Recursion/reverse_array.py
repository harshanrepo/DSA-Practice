def reverse_arr(arr):
    l=0
    r=len(arr)-1
    while l < r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

arr=[10,20,30,40,50]
print(reverse_arr(arr))