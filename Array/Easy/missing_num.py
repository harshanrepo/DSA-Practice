def missing_num(arrs):
    n=len(arrs)+1

    total_sum=sum(arrs)

    expect_sum=n*(n+1)//2

    print(total_sum)
    print(expect_sum)
    print(expect_sum-total_sum)

arrs=[8, 2, 4, 5, 3, 7, 1]
missing_num(arrs)