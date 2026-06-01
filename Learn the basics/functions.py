'''def urname(name):
    print(f"I'm {name}")

urname("Kren")'''

'''def addTwonum(a,b):
    return a+b

print("The add of a and b:",addTwonum(5,3))'''



def dosomething(num):
    num+=10
    print(num)
    num+=5
    print(num)

def number(num):
    print(num)
    dosomething(num)
    print(num)

number(10)