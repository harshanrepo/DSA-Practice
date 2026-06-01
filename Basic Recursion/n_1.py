def n_one(n,num):
    if n<num:
        return
    print(n,end=" ")
    n_one(n-1,num)
    
n_one(n=4,num=1)