def count_digit(n):
    # count=0
    # while n > 0:
    #     count+=1
    #     n=n//10
    # return count
    count=len(str(n))
    return count

n=7789
print(count_digit(n))