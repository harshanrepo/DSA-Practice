def numberright_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

n=5
numberright_triangle(n)