def one_N(i,n):
    if i>n:
        return
    print(i,end=" ")
    one_N(i+1,n)

i=1
n=5
one_N(i,n)