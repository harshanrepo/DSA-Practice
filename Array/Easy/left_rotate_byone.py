def left_rotate(arr):
    if len(arr) <1:
        return -1
    
    # right=arr[:1]
    # left=arr[1:]
    # result=left+right
    # return result

    temp_num=arr[0]

    for i in range(1,len(arr)):
        arr[i-1]=arr[i]

    arr[-1]=temp_num

    return arr

arr=[1, 2, 3, 4, 5] 
print(left_rotate(arr))
