# def prine_number(n):
#     is_prime=True

#     if n<=1:
#         is_prime=False
#     for i in range(2,n):
#         if i%2==0:
#             is_prime=False
#     return is_prime

# n=7
# print(prine_number(n))

def checkPrime(n):
    cnt = 0  
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1  
    return cnt == 2

n = 7 
isPrime = checkPrime(n)  

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")