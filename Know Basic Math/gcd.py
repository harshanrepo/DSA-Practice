def gcd(n1,n2):
    while n2:
      n1,n2=n2,n1%n2
    return n1
      
n1=9
n2=12
print(gcd(n1,n2))