def last_line():
    print("End of line...")
def icons(n):
    if n<=4:
        print(n)
        icons(n+1)
        
n=1
icons(n)
last_line()