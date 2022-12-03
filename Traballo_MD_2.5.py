####################################### Imports #######################################


####################################### Functions #######################################
def factorial_iterativa(n):
    toret = n
    for i in range (n-1,1,-1):
        toret *= i
    return toret

def factorial(n):
    if n <= 0:
        return 1    
    return n * factorial(n - 1)

def combinaciones_sin_repeticiones(n, r):
    combinacion = factorial(n) / (factorial(n-r)*factorial(r))
    return int(combinacion)

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

numPreguntas = input("¿Cuántas preguntas tiene el exámen? ").split()[0]
while not numPreguntas.isnumeric() or int(numPreguntas) <= 0:
    print("Debe escribir un número entero mayor que cero")
    numPreguntas = input("¿Cuántas preguntas tiene el exámen? ").split()[0]
numPreguntas = int(numPreguntas)    

temasEstudiados = input("¿Cuántas temas ha estudiado? ").split()[0]
while not temasEstudiados.isnumeric() or int(temasEstudiados) <= 0:
    print("Debe escribir un número entero mayor que cero")
    temasEstudiados = input("¿Cuántas temas ha estudiado? ").split()[0]
temasEstudiados = int(temasEstudiados)


# Calculamos las posibilidades sin repeticiones
if numPreguntas <= temasTotales:
    totalSinR = combinaciones_sin_repeticiones(temasTotales, numPreguntas)
    
    for i in range(numPreguntas+1):
        posibilidadesPreguntasEstudiadas = combinaciones_sin_repeticiones(temasEstudiados, i)
        posibilidadesPreguntasNoEstudiadas = combinaciones_sin_repeticiones(temasTotales-temasEstudiados, numPreguntas-i)
        conbinatoriaSinR.append(posibilidadesPreguntasEstudiadas*posibilidadesPreguntasNoEstudiadas)

# Calculamos las posibilidades con repeticiones
totalConR = combinaciones_con_repeticion(temasTotales, numPreguntas)
for i in range(numPreguntas+1):
    posibilidadesPreguntasEstudiadas = combinaciones_con_repeticion(temasEstudiados, i)
    posibilidadesPreguntasNoEstudiadas = combinaciones_con_repeticion(temasTotales-temasEstudiados, numPreguntas-i)
    conbinatoriaConR.append(posibilidadesPreguntasEstudiadas*posibilidadesPreguntasNoEstudiadas)

if numPreguntas <= temasTotales:
    for j, i in enumerate(conbinatoriaSinR):
        print(f"Las posibilidades de acertar {j} sin repetición son {i}")
else:
    print("No se puede calcular los porcentajes sin repetir temas porque hay más preguntas que temas.")


for j, i in enumerate(conbinatoriaConR):
        print(f"Las posibilidades de acertar {j} con repetición son {i}")


