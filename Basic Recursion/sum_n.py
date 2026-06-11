
 # Parameterised Recursion
'''def sum_n(i,sum):
    if i<1:
        print(sum)
        return
    sum_n(i-1,sum+i)

i=3
sum=0
sum_n(i,sum)'''

# Functional Recursion

def sum_n(sum):
    if sum==0:
        return 0
    return sum+sum_n(sum-1)

sum=3
print(sum_n(sum))