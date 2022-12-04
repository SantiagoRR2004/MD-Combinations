####################################### Imports #######################################


####################################### Functions #######################################
def factorial_iterativa(n):
    if n <= 0:
        return 1 
    toret = n
    for i in range (n-1,1,-1):
        toret *= i
    return toret

def factorial(n):
    if n <= 0:
        return 1    
    return n * factorial(n - 1)

def combinaciones_sin_repeticiones(n, r):
    if n > 900 or r > 900:
        return int(factorial_iterativa(n) / (factorial_iterativa(n-r)*factorial_iterativa(r)))
    return int(factorial(n) / (factorial(n-r)*factorial(r)))

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

if numPreguntas > temasTotales:
    print("No se puede calcular los porcentajes sin repetir temas porque hay más preguntas que temas.")
else:
    print("\nA continuación mostramos las probabilidades sin repetir temas en distintas preguntas del examen\n")
    for j, i in enumerate(conbinatoriaSinR):
        print(f"La probabilidad de acertar {j} preguntas es de {i/totalSinR*100:.2f}%")
    print("")
    for i in range(len(conbinatoriaSinR)-1):
        print(f"La probabilidad de acertar más de {i} preguntas es de {sum(conbinatoriaSinR[i+1:])/totalSinR*100:.2f}%")

print("\nA continuación mostramos las probabilidades repitiendo temas en distintas preguntas del examen\n")
for j, i in enumerate(conbinatoriaConR):
    print(f"La probabilidad de acertar {j} preguntas es de {i/totalConR*100:.2f}%")
print("")
for i in range(len(conbinatoriaConR)-1):
    print(f"La probabilidad de acertar más de {i} preguntas es de {sum(conbinatoriaConR[i+1:])/totalConR*100:.2f}%")
    


