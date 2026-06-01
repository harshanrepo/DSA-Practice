def second_largest(arr):
    n=len(arr)
    if n<1:
        return -1
    max=arr[0]
    second_max=0
    for i in range(n):
        if arr[i]>max:
            second_max=max
            max=arr[i]
        
        if arr[i] > second_max and arr[i]!=max:
            second_max=arr[i]

    print(second_max)

arr= [1, 2, 4, 7, 7, 5]  
second_largest(arr)