def reverse_righttriangle(n):
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(j,end=" ")
        print()

n=6
reverse_righttriangle(n)