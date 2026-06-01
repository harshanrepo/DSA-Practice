def decrease_letter(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end=" ")
        print()

n=3
decrease_letter(n)