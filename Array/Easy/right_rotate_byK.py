def right_rotate(arr,k=3):
    n = len(arr)
    k %= n

    arr.reverse()          
    arr[:k] = reversed(arr[:k])      
    arr[k:] = reversed(arr[k:])      

    return arr

arr=[1,2,3,4,5]
print(right_rotate(arr))