####################################### Imports #######################################


####################################### Functions #######################################
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

####################################### Variables #######################################
conbinatoriaSinR = []
conbinatoriaConR = []

####################################### Main Program #######################################
temasTotales = input("¿Cuántos temas entran en el exámen? ").split()[0]
while not temasTotales.isnumeric() or int(temasTotales) <= 0:
    print("Debe escribir un número entero mayor que cero")
    temasTotales = (input("¿Cuántos temas entran en el exámen? ").split())[0]
temasTotales = int(temasTotales)

    
n = input("¿Cuántas preguntas tiene el exámen? ").split()[0]
while not n.isnumeric() or int(n) <= 0:
    print("Debe escribir un número entero mayor que cero")
    n = input("¿Cuántas preguntas tiene el exámen? ").split()[0]

temasEstudiados = input("¿Cuántas temas ha estudiado? ").split()[0]
while not temasEstudiados.isnumeric() or int(temasEstudiados) <= 0:
    print("Debe escribir un número entero mayor que cero")
    temasEstudiados = input("¿Cuántas temas ha estudiado? ").split()[0]
