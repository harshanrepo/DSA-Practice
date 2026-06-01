def num_Crown(n):
    spaces=2*(n-1)
    for i in range(n):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,spaces+1):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
        spaces-=2

n=5
num_Crown(n)