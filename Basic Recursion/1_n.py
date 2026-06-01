def one_n(n,num):
    if num>n:
        return 
    print(num,end=" ")
    one_n(n,num+1)

one_n(n=4,num=1)