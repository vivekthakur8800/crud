def fibonacci(n):
    mydict={0:0,1:1}
    if n in mydict:
        return mydict[n]
    result=fibonacci(n-1) + fibonacci(n-2)
    mydict[n]=result
    return result

# print(fibonacci(50))

def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
# print(factorial(6))

sqaure=lambda n,m:n*m
# print(sqaure(6,5))