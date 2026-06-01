# Paramter way
'''def sum_n(n,sum):
    if n<1:
        print(sum)
        return
    sum_n(n-1,sum+n)

sum_n(n=3,sum=0)'''

# Functinal Way

def sum_n(n):
    if (n==0):
        return 0
    return n+sum_n(n-1)

print(sum_n(n=3))

