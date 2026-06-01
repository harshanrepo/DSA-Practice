def palindrome_num(n):
    org=n
    rev=0
    if n<0:
        return False
    while n>0:
        last=n%10
        rev=rev*10+last
        n=n//10
    if rev==org:
        return True
    else:
        return False

n=121
print(palindrome_num(n))