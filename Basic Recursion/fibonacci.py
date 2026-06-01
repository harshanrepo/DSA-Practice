def fibonacci(n):
    n1=0
    n2=1
    n3=0
    print(n1,n2,end=" ")
    while n>n3:
        n3=n1+n2
        n1,n2=n2,n3
        print(n3,end=" ")

fibonacci(n=5)
