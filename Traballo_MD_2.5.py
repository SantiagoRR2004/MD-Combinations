####################################### Imports #######################################
import matplotlib.pyplot as plt

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
    
plt.figure(figsize=(800,9))
plt.title(f"{temasTotales} temas, {numPreguntas} preguntas, {temasEstudiados} estudiados", fontsize=22)
plt.grid(zorder=-10)
plt.yticks([x for x in range(0,101,5)])
plt.ylim([0,101])
plt.xticks([x for x in range(numPreguntas+1)])

# Los prints comentados están para comprobar que funcione
if numPreguntas <= temasTotales:
##    print([x for x in range(numPreguntas+1)])
##    print([x/totalSinR*100 for x in conbinatoriaSinR])
    plt.scatter([x for x in range(numPreguntas+1)], [x/totalSinR*100 for x in conbinatoriaSinR], s=50, c="r", zorder=10, marker="o")
    plt.plot([x for x in range(numPreguntas+1)], [x/totalSinR*100 for x in conbinatoriaSinR], linewidth=5, c="r", zorder=0, label="Sin repetición\nacertar\nx preguntas")

##    print([x for x in range(numPreguntas)])
##    print([sum(conbinatoriaSinR[x+1:])/totalSinR*100 for x in range(len(conbinatoriaSinR)-1)])
    plt.scatter([x for x in range(numPreguntas)], [sum(conbinatoriaSinR[x+1:])/totalSinR*100 for x in range(len(conbinatoriaSinR)-1)], s=50, c="#FF00FF", zorder=10, marker="o")
    plt.plot([x for x in range(numPreguntas)], [sum(conbinatoriaSinR[x+1:])/totalSinR*100 for x in range(len(conbinatoriaSinR)-1)], linewidth=5, c="#FF00FF", zorder=0, label="Sin repetición\nacertar\nmás de x\npreguntas")

##print([x for x in range(numPreguntas+1)])
##print([x/totalConR*100 for x in conbinatoriaConR])
plt.scatter([x for x in range(numPreguntas+1)], [x/totalConR*100 for x in conbinatoriaConR], s=50, c="b", zorder=10, marker="o")
plt.plot([x for x in range(numPreguntas+1)], [x/totalConR*100 for x in conbinatoriaConR], linewidth=5, c="b", zorder=0, label="Con repetición\nacertar\nx preguntas")

##print([x for x in range(numPreguntas)])
##print([sum(conbinatoriaConR[x+1:])/totalConR*100 for x in range(len(conbinatoriaConR)-1)])
plt.scatter([x for x in range(numPreguntas)], [sum(conbinatoriaConR[x+1:])/totalConR*100 for x in range(len(conbinatoriaConR)-1)], s=50, c="#00FCFF", zorder=10, marker="o")
plt.plot([x for x in range(numPreguntas)], [sum(conbinatoriaConR[x+1:])/totalConR*100 for x in range(len(conbinatoriaConR)-1)], linewidth=5, c="#00FCFF", zorder=0, label="Con repetición\nacertar\nmás de x\npreguntas")









plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True, fancybox=True)
plt.xlabel("Preguntas")
plt.ylabel("Porcentajes")
##plt.savefig(CPUname+".svg")
plt.show()
