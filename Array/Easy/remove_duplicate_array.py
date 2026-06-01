'''def remove_duplicate(arr):
    seen=set()
    index=0

    for i in arr:
        if i not in seen:
            seen.add(i)
            arr[index]=i
            index+=1
    return seen

arr=[1,1,2,2,2,3,3]
print(remove_duplicate(arr))'''

# Leetcode

def remove_duplicate(arr):
    if not arr:
        return 0

    j=0 
    for i in range(1,len(arr)):
        if arr[i] !=arr[j]:
            j+=1
            arr[j]=arr[i]
    return arr[:j+1]

arr=[1,1,2]
print(remove_duplicate(arr))