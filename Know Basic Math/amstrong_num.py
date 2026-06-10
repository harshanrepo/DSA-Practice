def amstrong(n):
    org=n
    digit=len(str(n))
    sum=0
    while n > 0:
        last=n%10
        sum+=last**digit
        n=n//10
    return sum==org

n=153
print(amstrong(n))