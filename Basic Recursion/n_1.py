def N_one(i,n):
    if i<=0:
        return
    print(i,end=" ")
    N_one(i-1,n)
i=4
n=4
N_one(i,n)