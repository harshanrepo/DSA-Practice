def one_n_backtrack(i,n):
    if i<1:
        return
    one_n_backtrack(i-1,n)
    print(i,end=" ")

i=3
n=3
one_n_backtrack(i,n)