'''str="hello how are you"

def reverse_word(str):
    str=str.split()
    result=""
    for i in str:
        result+=i[::-1]+" "

    print(result)
reverse_word(str)'''

# def inverted_triangle(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end=" ")
#         print()

# n=4
# inverted_triangle(n)
        
# def inverted_triangle(n):
#     for i in range(n-1):
#         for j in range(1,n-i):
#             print(j,end=" ")
#         print()

# n=5
# inverted_triangle(n)


# accounts=[[1,5],[7,3],[3,5]]
# result=[]
# for i in accounts:
#     result.append(sum(i))
# print(max(result))

matrix=[[1,2,3],[4,5,6],[7,8,9]]


for i in range(len(matrix)):
    