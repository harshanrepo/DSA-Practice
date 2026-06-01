def letter_right(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print()


n=5
letter_right(n)