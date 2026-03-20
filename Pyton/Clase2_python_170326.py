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

### Desafíos sin solución ###
#1. Crea un generador de contraseñas usando operaciones de strings. 
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

#2. Desafío 2: Python tiene un tipo especial llamado complex para números complejos. Investiga cómo funciona y calcula (3+4j) * (1-2j).
#Se utiliza j para denominar un número complejo (imaginario). Se puede de dos formas
# Forma literal
z1 = 3 + 4j

# Usando la función
z2 = complex(2, -5)

print(z1)  # (3+4j)
print(z2)  # (2-5j)
#así se puede acceder a sus dos partes
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
#la operacion se puede hacer directamente
(3+4j) * (1-2j) #= (11-2j)
#resulta que para los números imaginarios, j^2 = -1, de ahí que de sentido el resultado anterior.

#3. ¿Qué pasa si intentas concatenar un string con un número directamente? 
#Investiga la diferencia entre "Valor: " + str(42) y f"Valor: {42}".
"Valor: " + str(42)
f"Valor: {42}"
#el resultado es el mismo, pero sin llamar la función str. En oraciones cortas puede funcionar, pero en oraciones más largas
#podría causar muchos errores. 


    
