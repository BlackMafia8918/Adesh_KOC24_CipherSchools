"""def sum(a):     
    if a > 100:                   #base case
        return
    print(a)
    a = 2*a
    sum(a)
    
    
sum(5)
"""


#Reducing -

#Case 1:

"""
def reduce(a):
    if a < 0:
        return
    print(a)
    a -= 1
    reduce(a)
    
reduce(5)
"""

#Demo function :

#Case 2:

#Power of 2 :-

"""
def demo(a):
    if a == 1:
        
        return 2
        
    return 2* demo(a-1)

print(demo(10))
"""

#Sum of list :-
"""
def sum(l, i):
    if i== len(l):
        return 0
    return l[i] + sum (l, i+1)

l=[1, 2, 3, 4, 5]
print(sum(l, -5))
"""

#Date - 15/10/2022
#Revision


"""
def demo(x):
    if x < 0:
        return
    
    print(x)
    demo(x-1)
    
demo(5)
"""


