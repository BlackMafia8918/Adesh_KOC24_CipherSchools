#Question 1
"""
I/p:
6
1
2
3
4
5
6
print the count of even and odd numbers in this list

o/p:
even numbers in list are: 3
odd numbers in list are: 3
"""


#Question 2

"""
I/p:

6
4 5 6 3 1 2

find out how many square of numbers are divisibly by both 3 and 2

o/p:
Count is: 1
"""



# SOLUTIONS -

#Question 1
"""
l=list(map(int,input().split(",")))

even_count=0

odd_count=0

for i in l:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("No. of even numbers:",even_count)
print("No. of odd numbers:",odd_count)
"""



"""
n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
    
countEven=0
countOdd=0
for i in l:
    if i%2==0:
        countEven+=1
    else:
        countOdd+=1
        
print("No. of even numbers:",countEven)
print("No. of odd numbers:",countOdd)
"""    
    

#Question 2
"""
l=list(map(int,input().split(",")))
count=0
for i in l:
    if ((i**2)%2==0) and ((i**2)%3==0):
        count+=1
        
print("Count is:",count)
"""


"""
n=int(input())
l = list(map(int, input(). split(" ")))
count=0

for i in l:
    y=i**2
    if y%2==0 and y%3==0:
        count += 1
        
print("Count is:",count)
"""

