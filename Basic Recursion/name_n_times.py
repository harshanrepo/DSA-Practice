def name_n_times(num,n):
    if num>=n:
        return 
    print("Kren",end=" ")
    name_n_times(num+1,n)

name_n_times(num=0,n=5)