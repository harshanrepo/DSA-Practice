def count_digit(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    print(count)

n=7789              
count_digit(n)