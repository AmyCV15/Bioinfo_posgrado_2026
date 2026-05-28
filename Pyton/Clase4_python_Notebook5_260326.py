## Notebook 5. Listas y sus moficaciones##



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



print("ab", sep="-")
print()


temperatura = [28, 30, 45, 70]
temp2 = sorted(temperatura)
temperatura.sort()
a = [1,2,3,4,5]
a*3


###########################333
#def define la función
# MINI PROYECTO: Calculadora de Índice de Masa Corporal (IMC)
def calcular_imc(peso_kg, altura_m):
    '''Calcula el IMC y retorna la clasificación.'''
    imc = peso_kg / (altura_m ** 2)
    
    if imc < 18.5:
        clasificacion = "Tienes bajo peso"
        emoji = "⬇️"
        consejo = "Considera aumentar tu ingesta calórica. Acude al departamento de nutrición en FCN"
    elif imc < 25:
        clasificacion = "Peso normal"
        emoji = "✅"
        consejo = "¡Mantén tus hábitos saludables!"
    elif imc < 30:
        clasificacion = "Sobrepeso"
        emoji = "⚠️"
        consejo = "Considera aumentar la actividad física. Acude al departamento de nutrición en FCN"
    else:
        clasificacion = "Obesidad"
        emoji = "🔴"
        consejo = "Consulta a un profesional de salud"
    
    return imc, clasificacion, emoji, consejo
  
calcular_imc(70, 1.70)


########
#Crea un clasificador de triángulos que, dadas 3 longitudes de lados, determine 
#si es equilátero, isósceles, escaleno, o si no forma un triángulo válido.
def clasf_triang(L1, L2, L3):
   '''Clasifica los triángulos de acuerdo a sus características.'''
   if L1 == L2 and L2 == L3:
     tipo = "Triángulo equilatero"
     caracteristicas = "todos sus lados son iguales"
   elif L1 == L2 or L1 == L3: 
     tipo = "Triangulo isóceles" 
     caracteristicas = "Solo dos de sus lados son iguales"
   else:
     tipo = "Triángulo escaleno"
     caracteristicas = "Todos sus lados son diferentes"
   return tipo, caracteristicas

clasf_triang(2, 2, 2)

# Función con parámetros
def saludar_persona(nombre, lenguaje="Python"):
    """Saluda a una persona mencionando su lenguaje favorito.
    
    Args:
        nombre: El nombre de la persona
        lenguaje: Lenguaje favorito (por defecto: Python)
    """
    print(f"¡Hola, {nombre}! Veo que programas en {lenguaje}.")

saludar_persona("Amy", "R")

# Funciones que retornan valores
def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo."""
    return ancho * alto

# El valor retornado puede usarse directamente
area = calcular_area_rectangulo(10, 5)
print(f"Área: {area} m²")

# O en expresiones
if calcular_area_rectangulo(3, 4) > 10:
    print("El rectángulo es grande")

# Retorno múltiple (usando tupla)
import math
def estadisticas(numeros):
    """Retorna estadísticas básicas de una lista."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

datos = [15, 8, 23, 42, 4, 16]
minimo, maximo, promedio = estadisticas(datos)
print(f"Min: {minimo}, Max: {maximo}, Promedio: {promedio:.1f}")

#calculadora 
def calculadora(n1, n2):
 return n1 + n2, n1*n2, n1-n2, n1/n2

resultado = calculadora(2, 3)
print(f"Tus resultados son: {resultado}")

n1 = 2
n2 = 3
suma, multiplicacion, resta, division = calculadora(n1, n2)
print(f"Suma: {suma}; Multiplicación: {multiplicacion}; Resta: {resta}; Division: {division}")
