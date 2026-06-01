def invert_star_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*n-(2*i+1)):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        print()

n=5
invert_star_pyramid(n)