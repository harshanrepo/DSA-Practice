def reverse_righttriangle(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        print()

n=5
reverse_righttriangle(n)