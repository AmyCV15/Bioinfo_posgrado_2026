x = 3
print(x)
saludo1 = "Hola, mundo"
saludo2 = 'Hola, mundo'

print(saludo1 == saludo2)    # True
numero_enorme = 2 ** 100
print(f"2^100 = {numero_enorme}")
print(f"Dígitos: {len(str(numero_enorme))}")

print
nombre = "Amairani"  
edad = 26
altura = 1.73
es_estudiante = True 
print(f"\nTipos:")
print(f"  mi nombre es:        {nombre}")
print(f"  mi edad es:          {edad}")
print(f"  altura:        {altura}")
print(f"  es estudiante: {es_estudiante}")


#Ejercicio 
ciudad = "Querétaro"
lenguaje_previo = "R"
print(f"Hola, mi nombre es {nombre}, tengo {edad} años, vivo en {ciudad} y mi lenguaje aprendido es {lenguaje_previo}")


## segundo ejercicio 
año_actual =2026
año_nacimiento = 1999
edad_actual = 2026 - 1999
edad_2030 = 2030 - año_nacimiento
es_mayor = edad_actual >= 18
print(f"Mi edad actual es: {edad_actual} años. Mi edad en 2030 será: {edad_2030} años ")

#Ejercicio 3
celsius = 45
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
print(f"{celsius}°C equivalen a {kelvin:.2f}K")

#ejercicio 4
peso = 70    # kg
altura = 1.75  # metros

# Calculá el IMC:
imc = peso / altura ** 2

if imc <= 18.4:
  print("Tienes bajo peso")
if imc > 18.5:  # no pues todavía no me salen estos. 
  print("estas saludable")

print(f"De acuerdo a tu peso de {peso}kg y tu altura de {altura}m, tu indice de masa corporal es {imc:.2f}")


#ejercicio 4
numero = 7
print(f"{numero} × 1 = {numero * 1}")
print(f"{numero} × 2 = {numero * 2}")
print(f"{numero} × 3 = {numero * 3}")
print(f"{numero} × 4 = {numero * 4}")
print(f"{numero} × 5 = {numero * 5}")



### Ejercicios de tarea: Introducción a Pyton ###
#Nivel 1: Fundamentos 
#1.1 Crea variables para tu nombre, edad, ciudad y lenguaje previo.
# Luego imprimí una presentación usando f-strings.
nombre = "Amairani"
edad = 27
ciudad = "Lázaro Cárdenas"
lenguaje_previo = "R studio"
print (f"¡Hola! Mi nombre es {nombre}, tengo {edad} años y vengo de {ciudad}. Mi lenguaje de programacion previo es {lenguaje_previo}.")

#1.2 Dado tu año de nacimiento, calcula y muestra:
# - Tu edad actual (asumí 2026)
# - Tu edad en 2030
# - El año en que cumplirás 100 años
# - Si sos mayor de edad (>= 18)
año_actual =2026
año_nacimiento = 1999
edad_actual = año_actual - año_nacimiento
edad_2030 = 2030 - año_nacimiento
es_mayor = edad_actual >= 18
edad_cien_años = año_nacimiento + 100

print(f"Mi edad actual es: {edad_actual} años. Mi edad en 2030 será: {edad_2030} años. El año en el que cumpliría 100 años es en {edad_cien_años}")
print(f"¿Eres mayor de edad? {es_mayor}")

#1.3
# Convertí 100 grados Celsius a:
# - Fahrenheit: F = C × 9/5 + 32
# - Kelvin: K = C + 273.15
# Mostrá todos los resultados con 2 decimales
celsius = 100
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
print(f"{celsius}°C equivalen a {kelvin:.2f}K")

#Nivel 2: Aplicación
#2.1 Calcula el Índice de Masa Corporal (IMC)
# Fórmula: IMC = peso(kg) / altura(m)²
#
# Mostrá:
# - El IMC redondeado a 1 decimal
# - Si el IMC indica: Bajo peso (<18.5), Normal (18.5-24.9),
#   Sobrepeso (25-29.9), u Obesidad (>=30)
peso = 70
altura = 1.75  
imc = peso / altura ** 2
imc_bajo = imc<18.5
imc_normal = imc > 18.5 <24.9
imc_sobrepeso = imc> 25 <29.9
imc_obesidad = imc >= 30
print(f"De acuerdo a tu peso de {peso}kg y tu altura de {altura}m, tu IMC es {imc:.1f}")
print(f"De acuerdo a tu valor de IMC, este cae en la categoía de Bajo: {imc_bajo}")
print(f"Normal: {imc_normal}; Sobrepeso: {imc_sobrepeso}; Obesidad: {imc_obesidad}")

#2.2
# Sin usar bucles (los veremos en el capítulo 4),
# imprimir los primeros 5 múltiplos de un número usando print() y f-strings.
numero = 11
print(f"{numero} × 1 = {numero * 1}")
print(f"{numero} × 2 = {numero * 2}")
print(f"{numero} × 3 = {numero * 3}")
print(f"{numero} × 4 = {numero * 4}")
print(f"{numero} × 5 = {numero * 5}")

#2.3 
# En Python, los strings soportan multiplicación: "=" * 10 → "=========="
# Usá esto para crear una función de separador visual.
#
# Creá variables para:
# - titulo: el texto del título
# - ancho: ancho total del separador (ej: 50)
# - caracter: el caracter del borde (ej: "=")
titulo = "Tarea 1 de introducción a Pyton"
ancho = 80
caracter = "="
margen = caracter * ancho
titulo_centrado = titulo.center(ancho) #.center ayuda a centrar en pantalla lo que sea 
print(margen)                          #que haya puesto en el objeto que indico. 
print(titulo_centrado)                 #al darle en este caso el valor de "ancho", agrega esa cantidad de "espacios"
print(margen)

#Nivel 3: Integración
# Dado un radio, calculá y mostrá en un reporte bien formateado:
# - Área del círculo
# - Perímetro (circunferencia)
# - Área de la esfera con ese radio: 4 × π × r²
# - Volumen de la esfera: (4/3) × π × r³
# Usá math.pi para mayor precisión y todos los resultados con 4 decimales
#importando math
import math #es como una librería con constantes numéricas
radio = 5
perimetro = 2 * math.pi * radio
area = math.pi * radio**2
area_esfera = 4 * math.pi * radio**2
volumen_esfera = (4/3) * math.pi * radio**3
print(f"De acuerdo al radio de {radio}cm, los valores calculados son: ")
print(f"Perimétro = {perimetro:.4f}cm")
print(f"Área = {area:.4f}cm^2")
print(f"Área de la esfera = {area_esfera:.4f}cm^2")
print(f"Volumen de la esfera = {volumen_esfera:.4f}cm^3")
#de acuerdo a la solución mostrada en la tarea:

#print(f"{'Área del círculo:':<25} {area:>12.4f}") #: indican que vienen indicaciones para formato de print
# < alineación a la izquierda 
# > alineación a la derecha 
# 12 es el tamaño total del espacio reservado, esto toma en cuenta el espacio necesario para todo el print indicado
#O sea "Área del círculo" tiene 17 caracteres (sí, los acentos también cuentan)
#por lo que solo quedan 8 caracteres disponibles para espacio de alineación
#objetivo: alinear todos los números igual.

#3.2 
# Dado un valor en kilómetros, convertilo a:
# - Metros (× 1000)
# - Centímetros (× 100000)
# - Millas (÷ 1.60934)
# - Pies (× 3280.84)
# - Pulgadas (× 39370.1)
#
# Presentalo en una tabla formateada con f-strings
# Alineá los números a la derecha con 2 decimales
km = 25
metros = km *1000
centimetros = metros * 100
millas = km/1.60934
pies = metros * 3.28
pulgadas = centimetros *2.54
#resultado en tabla formateada 
print("=" * 80)
print(f"{'Conversiones':^45}")
print("=" * 80)
print(f"Para el valor de {km} km:")
print(f"{'Metros = ':<12} {metros:>12.2f} m")
print(f"{'Centimetros = ':<12} {centimetros:>12.2f} cm")
print(f"{'Millas = ':<12} {millas:>11.5f} mi")
print(f"{'Pies = ':<12} {pies:>12.2f} ft")
print(f"{'Pulgadas = ':<12} {pulgadas:>14.2f} inch")

## Mi proyecto: Reporte de análisis básico ##
#Reporte de Inversión Simple
# Simula el cálculo de interés compuesto y genera un reporte.
#
# Fórmula: A = P × (1 + r/n)^(n×t)
# Donde:
#   P = capital inicial
#   r = tasa anual (decimal)
#   n = número de veces que se compone por año
#   t = tiempo en años

# Datos de la inversión
nombre_inversor = "Amairani Chávez"
capital_inicial = 10000     # pesos
tasa_anual = 0.08      # 8% anual
n_composicion = 12        # mensual
años = 5

# Cálculo
monto_final = capital_inicial * (1 + tasa_anual / n_composicion) ** (n_composicion * años)
ganancia    = monto_final - capital_inicial
rendimiento = (ganancia / capital_inicial) * 100

print("=" * 80)
print(f"{'Reporte de inversión simple de':^50} {nombre_inversor}")
print("=" * 80)
print(f"Capital inicial: ${capital_inicial}, con una tasa anual de {tasa_anual}, proyectado a {años} años")
print(f"Con los siguientes resultados:")
print(f"{'Monto final = ':<12} {monto_final:>14}")  #por que en la segunda parte no se vuelve a usar ' ' 
print(f"{'Ganancia = ':<12} {ganancia:>18}")
print(f"{'Rendimiento = ':<12} {rendimiento:>14}")

#como funciona la primer espaciada?


###Desafíos ####

