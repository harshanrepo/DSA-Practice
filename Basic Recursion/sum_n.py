def sum_n(i,sum):
    if i<1:
        print(sum)
        return
    sum_n(i-1,sum+i)

i=3
sum=0
sum_n(i,sum)
