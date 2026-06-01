def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

n=4
square_pattern(n)