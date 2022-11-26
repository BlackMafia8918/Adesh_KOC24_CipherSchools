"""def maxElement(a,b):
    if a>b:
        return a
    else:
        return b
    
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
maxE = maxElement(a,b)
print("Maximum element is:" , maxE)"""


def sumoflist(l):
    sum = 50
    for i in l :
        sum = sum + i
        return sum
    
l = [1,5,4,3,3,1]
sum=sumoflist(l)
print (sum)