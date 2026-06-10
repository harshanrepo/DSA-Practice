def palindrome_num(n):
    org=n
    rev=0
    while n > 0:
        last=n%10
        rev=rev*10+last
        n=n//10
    return rev==org

n=1212
print(palindrome_num(n))