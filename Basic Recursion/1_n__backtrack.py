def one_to_n(n):
    if (n<1):
        return 
    one_to_n(n-1)
    print(n,end=" ")

one_to_n(n=4)
