def gcd_num(n1,n2):
    # gcd=1
    # for i in range(1,min(n1,n2)+1):
    #     if n1%i==0 and n2%i==0:
    #         gcd=i
    # return gcd

    while n1>0 and n2>0:
        if n1==0:
            return n2
        if n1>n2:
            n1=n1%n2
        else:
            n2=n2%n1
        return n1

n1,n2=20,15
print(gcd_num(n1,n2)) 
