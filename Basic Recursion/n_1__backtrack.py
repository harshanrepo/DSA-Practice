def one_to_n(n,num):
    if num>n:
        return 
    one_to_n(n,num+1)
    print(num,end=" ")

one_to_n(n=3,num=1)
