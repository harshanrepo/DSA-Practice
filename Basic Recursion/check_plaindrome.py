def check_plaindrome(i,s):
    n=len(s)
    if i >=n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return check_plaindrome(i+1,s)

i=0
s="MADAM"
print(check_plaindrome(i,s))