def fibonacci(n):
    if n <= 1:
        return n
    last = fibonacci(n - 1)  
    slast = fibonacci(n - 2)  
    return last + slast

n = 4
print(fibonacci(n)) 
