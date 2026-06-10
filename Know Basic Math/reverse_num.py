def reverse_num(n):
    rev=0
    while n > 0:
        last=n%10
        rev=rev*10+last
        n=n//10
    return rev

n=12345
print(reverse_num(n))