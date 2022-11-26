#Factorial -


#1-
"""
def factorial(n):
    if n==0:
        return 1
    
    return n * factorial (n-1)
        
print(factorial(10))
"""

#2-

"""
def fact(n) :
    c=1
    if n==0:
        print("1")
    else:
        while n>0:
            c*=n
            n-=1
            print(c)

a=int(input("factorial: "))
fact(a)
"""

#3-

"""
i=1
def f(n):
    if n<0:
        return
    elif n ==0:
        return 1
    else:
        return n*f(n-1)

a = int(input("Enter a number:"))
print(f(a))
"""

#4 -
"""
def f(n):
    if n<0:
        return "Factorial cant be found"
    elif n ==0:
        return 1
    else:
        return n*f(n-1)

a = int(input("Enter a number:"))
print(f(a))
"""


