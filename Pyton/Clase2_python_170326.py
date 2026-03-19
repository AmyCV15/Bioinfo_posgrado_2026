#Clase2_pyton_190326

##Una cadena de texto se llama string
#Ejercicios prácticos 
# Ejercicio 2.1
# Dada esta variable con formato inconsistente:
nombre_sucio = "  jUaN pEDro GoNZÁLEz  "

# Realiza las siguientes operaciones:
# 1. Elimina los espacios extra
# 2. Convierte a formato título (cada palabra capitalizada)
# 3. Muestra solo el primer nombre en mayúsculas)
nombre_limpio = nombre_sucio.strip().title()
primer_nombre = nombre_limpio.split()[0].upper()
primer_nombre


#Desafíos sin solución
#Crea un generador de contraseñas usando operaciones de strings. 
#La contraseña debe tener el formato: [Inicial_nombre][Año_nacimiento][Símbolo][4_letras_apellido].
nombre = "Amairani"
letra_uno = nombre.split()
año_nacimiento = "1999"
símbolo = "$"
apellido = "Chávez"
nombre[0]
contraseña = nombre[0]+año_nacimiento+símbolo+apellido[0:3]
contraseña
#si quisiera dejar el año de nacimiento como numero se realiza esto:
contraseña_2 = f"tu contraseña es {nombre[0]}{año_nacimiento}{símbolo+apellido[0:3]}"



## notebook 3.

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
tareas = ['Revisar email', 'Escribir reporte', 'Reunión 3pm', 
          'Almorzar', 'Revisar código']

print("=== LISTA DE TAREAS ===")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")


#De la versión extendida: Ejercicios
# Ejercicio 1.1
# Crea una lista con los nombres de 5 países de América Latina.
# Luego:
# a) Imprime el primer y el último país usando índices positivos y negativos
# b) Imprime los 3 países del centro
# c) Imprime el número total de países en la lista

# Tu código aquí:
paises = ["Mexico", "Chile", "Belice", "Guatemala", "Brasil"]   # Llenar con 5 países
paises[0:-1]

# Ejercicio 1.2
# Dada esta lista de temperaturas semanales (lunes a domingo)
temperaturas = [18, 22, 19, 25, 28, 30, 27]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# a) ¿Cuál fue la temperatura del miércoles?
# b) ¿Cuáles fueron las temperaturas del fin de semana? (usando slicing)
# c) ¿Cuál fue la temperatura más alta y en qué día ocurrió?
# d) ¿Cuál fue el promedio de la semana? (redondea a 1 decimal
temp_alta = temperaturas.sort()
dias_temp = dias[0]+temperaturas[0]
sumatoria = sum(temperaturas) / len(temperaturas)
import statistics
#ya con el paquete
promedio2 = statistics.mean(temperaturas)



# Ejercicio 3.1
# Construye un reporte de calificaciones con formato profesional

alumnos = ['Sofía', 'Miguel', 'Valeria', 'Diego', 'Camila','Andrés', 'Fernanda', 'Ricardo', 'Lucía', 'Emilio']
califs  = [88, 72, 95, 61, 84, 79, 91, 67, 76, 83]

# a) Muestra el reporte ordenado por calificación (descendente)
#    con formato: posición, nombre, calificación, letra (A≥90, B≥80, C≥70, D<70)
# b) Muestra las estadísticas del grupo:
#    promedio, mínima, máxima, aprobados (≥70), reprobados
# c) Muestra los alumnos en orden alfabético con su calificación

# Tu código aquí:
print(f"{alumnos.sort")


## ejercicios del 5
temperatura = 28
humedad     = 75
dia_laboral = True
lluvia = 60

# and — ambas condiciones deben ser True
if temperatura > 20 and humedad < 60 and lluvia < 20:
    print("Clima perfecto para salir, la probabilidad de lluvia es de {lluvia}")
elif temperatura > 20 and humedad >= 60 and lluvia > 40:
    print("Caluroso y húmedo")   # ← se ejecuta este
else:
    print("Mejor quedarse en casa")
    
