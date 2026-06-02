def max_one(arr):
    cnt=0
    max_count=0

    for i in range(len(arr)):
        if arr[i]==1:
            cnt+=1
        else:
            cnt=0
        
        max_count=max(cnt,max_count)
    return  max_count

arr=[1,1,0,1,1,1]
print(max_one(arr))