def move_zeros(arrs):
    n=len(arrs)
    # if n<=1:
    #     return arrs
    # non_zeros=[]
    # index=0
    # for arr in arrs:
    #     if arr !=0:
    #         non_zeros.append(arr)
    #         index+=1
    # while index < n:
    #     non_zeros.append(0)
    #     index+=1
    # return non_zeros


    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr

arr=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(move_zeros(arr))

