# fibonacci Series -

#1-

"""
def fibonacciTerm(n):
    if n==0 or n==1:
        return n
    
    return fibonacciTerm(n-1) + fibonacciTerm(n-2)


print(fibonacciTerm(50))

"""

#2-


def fibonacciSeries(n):
    a=0
    b=1
    if n == 0 or n== 1:
        print(n)
        return
    print(0 , "th term is: ", a)
    print(1 , "th term is: ", b)
       
    i=2
    while i<n:
        c=a+b
        print(i , "th term is: ", c)
        a=b
        b=c
        i += 1
        
       
fibonacciSeries(11)