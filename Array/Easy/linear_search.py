def linear_search(arrs,num):

    for i in range(len(arrs)):
        if arrs[i]==num:
            return i
    return -1

arrs=[5,4,3,2,1]
num=5
print(linear_search(arrs,num))
