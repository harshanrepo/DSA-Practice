def all_divisor(n):
    values=[]
    for i in range(1,n+1):
        if n % i ==0:
            values.append(i)
    return values

n=12
print(all_divisor(n))