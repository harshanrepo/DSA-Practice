def n_one_backtrack(i,n):
    if i>n:
        return
    n_one_backtrack(i+1,n)
    print(i,end=" ")

i=1
n=3
n_one_backtrack(i,n)

