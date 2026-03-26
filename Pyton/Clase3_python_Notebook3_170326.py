## Notebook 3. Listas y sus moficaciones##

#Ejercicios
#3.1
# Tienes una lista de invitados a una cena
invitados = ['María', 'Carlos', 'Ana', 'Pedro']

# 1. Muestra un mensaje personalizado para cada invitado
for invitado in invitados:
    print(f"Estimado/a {invitado}, te invitamos a nuestra cena especial.")
# 2. Pedro no puede venir, reemplázalo por Laura
invitados[invitados.index('Pedro')] = 'Laura'
print(f"Lista actualizada: {invitados}")
# 3. Conseguiste una mesa más grande, agrega 2 personas más
invitados.append('Roberto')
invitados.insert(0, 'Elena')
print(f"Lista final: {invitados}")
print(f"Total de invitados: {len(invitados)}")


# Ejercicio 3.2 — Sistema de tareas simple
tareas = ['Revisar email', 'Escribir reporte', 'Reunión 3pm', 'Almorzar', 'Revisar código']

print("=== LISTA DE TAREAS ===")
for i, tarea in enumerate(tareas, 1): 
    print(f"{i}. {tarea}")

#" " " 
#lo que está haciendo el programa aquí es primero enumerar las tareas comenzando por el 1.
#Y después i va tomando cada cosa que enumerate ya realizó (colcar 1 al primer elemento, 2 al segundo y así)
#i es un enumerador (iterador) que indica dar las "vueltas". Se realiza una acción indicada para cada elemento del objetivo indicado.

#" " " 
# Ordenar alfabéticamente
tareas_ordenadas = sorted(tareas)
print("=== TAREAS ORDENADAS ===")
for i, tarea in enumerate(tareas_ordenadas, 1):
    print(f"{i}. {tarea}")

# Completar primera tarea
completada = tareas.pop(0)
print(f"Tarea completada: {completada}")
print(f"Tareas restantes: {len(tareas)}")


#De la versión extendida: Ejercicios
# Ejercicio 1.1
# Crea una lista con los nombres de 5 países de América Latina.
paises = ["Mexico", "Chile", "Belice", "Guatemala", "Brasil"]
# a) Imprime el primer y el último país usando índices positivos y negativos
print(f"Primer país: {paises[0]}, último país: {paises[-1]}")
# b) Imprime los 3 países del centro
print(f"Países del centro de la lista: {paises[1:4]}")
# c) Imprime el número total de países en la lista
print(f"El número total de países de la lista es: {len(paises)}")

# Ejercicio 1.2
# Dada esta lista de temperaturas semanales (lunes a domingo)
temperaturas = [18, 22, 19, 25, 28, 30, 27]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
# a) ¿Cuál fue la temperatura del miércoles?
print(f"Temperatura del día miércoles fue de: {temperaturas[2]}°C")
# b) ¿Cuáles fueron las temperaturas del fin de semana? (usando slicing)
print(f"Las temperaturas del fin de semana fueron {temperaturas[4:7]}°C para Viernes, sábado y domingo, respectivamente")
# c) ¿Cuál fue la temperatura más alta y en qué día ocurrió?
temp_max = max(temperaturas)
temperaturas.index(temp_max)
print(f"El {dias[5]} fue el día con la mayor temperatura de la semana con {temp_max}°C")
# d) ¿Cuál fue el promedio de la semana? (redondea a 1 decimal)
temp_alta = temperaturas.sort()
sumatoria = sum(temperaturas) / len(temperaturas)
print(f"El promedio de temperaturas de la semana fue de {sumatoria:.1f}°C")
import statistics
#ya con el paquete
promedio2 = statistics.mean(temperaturas)


# Ejercicio 3.1
# Construye un reporte de calificaciones con formato profesional
alumnos = ['Sofía', 'Miguel', 'Valeria', 'Diego', 'Camila','Andrés', 'Fernanda', 'Ricardo', 'Lucía', 'Emilio']
califs  = [88, 72, 95, 61, 84, 79, 91, 67, 76, 83]
zip(alumnos, califs)
# a) Muestra el reporte ordenado por calificación (descendente)
#    con formato: posición, nombre, calificación, letra (A≥90, B≥80, C≥70, D<70)
lista_juntos = []
for nombre, nota in zip(alumnos, califs):
    juntos = f"{nombre:<12} | {nota:>12}"
    lista_juntos.append(juntos)

lista_juntos.sort(reverse = True)
  lista_juntos.insert(0, "Nombres")
print("\n".join(lista_juntos))
#### hasta aquí lo que yo intenté ####
# b) Muestra las estadísticas del grupo:
#    promedio, mínima, máxima, aprobados (≥70), reprobados
# c) Muestra los alumnos en orden alfabético con su calificación
# Crear pares y ordenar por calificación
pares = list(zip(alumnos, califs))
pares_ordenados = sorted(pares, key=lambda x: x[1], reverse=True)
#lo que se hace aquí es... al parecer cada pareja de nombre-numero es una X
#x[0] = nombre
#x[1] = numero
#entonces dentro de la función key=lambda x: x[1] se le dice que ordene pares_ordenados, pero solo tomando en cuenta 
#los numeros de cada par, la segunda parte del objeto x
# a) Reporte por posición 
print("=" * 45)
print(f"{'REPORTE DE CALIFICACIONES':^45}")
print("=" * 45)
print(f"{'Pos':<5}{'Nombre':<12}{'Calif':>6}{'  Letra'}")
print("-" * 45)
for i, (nombre, c) in enumerate(pares_ordenados, 1):
    letra = 'A' if c >= 90 else 'B' if c >= 80 else 'C' if c >= 70 else 'D'
    print(f"{i:<5}{nombre:<12}{c:>6}  {letra}")

# b) Estadísticas
print("=" * 45)
aprobados  = sum(c >= 70 for c in califs)
reprobados = len(califs) - aprobados
promedio   = sum(califs) / len(califs)
print(f"Promedio:   {promedio:.1f}")
print(f"Máxima:     {max(califs)}")
print(f"Mínima:     {min(califs)}")
print(f"Aprobados:  {aprobados}")
print(f"Reprobados: {reprobados}")

# c) Orden alfabético
print("\n" + "-" * 30)
print("ORDEN ALFABÉTICO")
pares_alfa = sorted(pares, key=lambda x: x[0])
for nombre, c in pares_alfa:
    print(f"  {nombre:<12} {c}")


#### Desafios ####
# 1. Dada una lista de 15 números aleatorios entre 1 y 100, calcula:
#Media, mediana (elemento central de la lista ordenada) y moda (valor que más se repite)
#Sin usar statistics ni NumPy — solo métodos de lista y operaciones básicas
#Tip para la mediana: ordena la lista y toma el elemento del índice len//2 :::

#para poder usar funcion para numero aleatorios
import random
numeros = random.sample(range(1, 101), 5)
#hay que decirle a random.sample de dónde sacar los números que estamos solicitando
#si tuviera un objeto tipo lista con varios numeros: random.saple(lista, 5)
#con range() le digo de donde darme los numero sin crear el objeto con 100 numeros
#hasta 101 porque en pyton no se toma en cuenta el último
print(numeros)
media_numeros = sum(numeros) / len(numeros)
print(media_numeros)
numeros_ordenados = sorted(numeros)
mediana = len(numeros_ordenados)//2
print(mediana) #esto me da 2, es decir, la posición 2 de la lista de núemeros.
#RECUERDA: que en pyton, el primer número se considera como posición 0...
#Aquí no hay numeros repetidos, pero si quisiéramos hacer eso:
#conteo = []
#for n in numeros:
 #   if n in conteo:
        conteo[n] = conteo[n] + 1
   # else:
    #    conteo[n] = 1

#print(conteo)


#2. Eliminar duplicados manualmente: Dada la lista [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 
#elimina todos los duplicados preservando el orden de primera aparición. Solo puedes 
#usar operaciones de lista, no set(). Muestra cuántos elementos únicos hay 
lista_numeros =[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for n in lista_numeros:
  if lista_numeros[n] = lista_numeros[n]:
    lista_numeros.remove(n)
#Pues esto no funciona
numeros_duplicados = [] #SE TIENE QUE USAR ESTOS CORCHETES PARA QUE SEA UNA LISTA.
for n in lista_numeros:
    if n not in numeros_duplicados:
        numeros_duplicados.append(n)

print(f"Lista original: {lista_numeros}")
print(f"Sin duplicados: {numeros_duplicados}")

#4. — Implementa una rotación de lista: mueve todos los elementos N posiciones 
#a la derecha, y los que salen por la derecha reaparecen por la 
#izquierda. Ejemplo: [1,2,3,4,5] rotado 2 → [4,5,1,2,3] Solo usa pop(), insert() y un loop manual (no slicing)
sin_rotar = [1, 2, 3, 4, 5, 7]
rotaciones = 3
for i in range(rotaciones):
    ultimo = sin_rotar.pop()
    sin_rotar.insert(0, ultimo)
print(sin_rotar)  

    
    

