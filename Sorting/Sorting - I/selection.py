
# Find minimum then swap.

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr

# arr=[13,46,24,52,20,9]
# print(selection_sort(arr))


# Recursion.

def selection_sort(arr,start=0):
    n=len(arr)
    
    if start>n-1:
        return
    
    min_index=start

    for i in range(start+1,n):
        if arr[i]<arr[min_index]:
            min_index=i
    arr[start],arr[min_index]=arr[min_index],arr[start]
    selection_sort(arr,start+1)
    return arr

arr=[13,46,24,52,20,9]
print(selection_sort(arr))