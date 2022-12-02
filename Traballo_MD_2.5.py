def factorial_iterativa(n):
    toret = n
    for i in range (n-1,1,-1):
        toret *= i
    return toret

def factorial(n):
    if n == 0:
        return 1    
    return n * factorial(n - 1)

def combinaciones_sin_repeticiones(n, r):
    combinacion = factorial(n) / (factorial(n-r)*factorial(r))
    return combinacion

def combinaciones_con_repeticion(n, r):
    return combinaciones_sin_repeticiones(n+r-1, r)
