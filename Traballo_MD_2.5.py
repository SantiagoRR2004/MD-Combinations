def factorial_iterativa(n):
    toret = n
    for i in range (n-1,1,-1):
        toret *= i
    return toret

def factorial(n):
    if n == 1:
        return(1)    
    return n * factorial(n - 1)
