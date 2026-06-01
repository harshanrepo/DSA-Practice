def palindrome_check(str):
    org=str
    rev=str[::-1]
    return org==rev

str="ABCDCBA"
result=palindrome_check(str)
if result:
    print("Palindrome...")
else:
    print("Not Palindrome...")