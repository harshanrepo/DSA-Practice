def half_diamond(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
    
    for i in range(n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        print()

n=4
half_diamond(n)