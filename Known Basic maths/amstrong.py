def amstrong_num(num):
    org=num
    cnt=len(str(num))
    sum=0
    n=num
    while n>0:
        last=n%10
        sum+=last**cnt
        n=n//10
    
    return sum==org

num=113
print(amstrong_num(num))

