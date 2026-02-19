##############
#### Ejercicios de capitulo 4 ###
# Ejercicio piloto. ¿Cómo se llenaría una matriz vacia a partir de vectores?
vector1 <- 1:10
vector2 <- 11:20
y <- matrix(nrow=5,ncol=2)
y
y[1,1] <- vector1[1]
y[2,1] <- vector1[2]
y[3,1] <- vector1[3] #y así sucesivamente pero no lo voy a hacer. 
#¿Qué pasaría si la longitud del vector es diferente a la columna o renglón 
#de la matriz? ¿Cómo podrías emplear cbind() & rbind()?`
matriz <- rbind(vector1, vector2)
matriz
m2 <- cbind(y, vector1)
m2 #nop así no


# Ejercicio 1. Genera dos matrices aleatorias de tamaño  3 × 3 y 
#luego suma ambas matrices.
M1 <- matrix(c(1:9), nrow = 3, ncol = 3)
M1
M2 <- matrix(c(10:18), nrow = 3, ncol = 3)
M2
M1 + M2

# Ejercicio 2. Crea dos matrices aleatorias, una de tamaño 2 x 3 y otra de 
#tamañano 3 x 4. Luego, calcula su producto matricial.
M3 <- matrix(c(1:6), nrow = 2, ncol = 3)
M4 <- matrix(c(1:12), nrow = 3, ncol = 4)
M3; M4
M3 %*% M4

# Ejercicio 3. Crea una matriz aleatoria de tamaño  4×3 y encuentra su 
#matriz transpuesta.
M4.1 <- matrix(c(1:12), nrow = 4, ncol = 3)
M4.1
t(M4.1)

#Ejercicio 4. Genera una matriz cuadrada aleatoria de tamaño  4×4 y calcula su determinante.
M5 <- matrix(sample(1:100, 16), nrow = 4, ncol = 4)
M5
det(M5) #esta función permite calcular la determinate de una matriz, debido a 
        #que el número de operaciones aumenta cuando son matrices mayores a 3x3.

# Ejercicio 5. Crea una matriz cuadrada aleatoria de tamaño 3x3 y encuentra su 
#inversa
M2 #voy a trabajar con esta matriz previamente creada
# para calcular el inverso de una matriz se necesita un determinante mayor a 0
det(M2) #número muy pequeño
M2.1 <- matrix(sample(1:20, 9), nrow = 3, ncol = 3)
M2.1
det(M2.1) #det mayor a 0. 
#existe la función solve 
M2.1_Inv <- solve(M2.1)
M2.1_Inv
#si se multiplica la matriz original por la inversa, deberíamos obtener la M identidad
M_indentidad <- M2.1 %*% M2.1_Inv
round(M_indentidad, 2) #para reondear los decimales y poder obtener una matriz más limpia

# Ejercicio 6. Genera una matriz aleatoria de tamaño  5x5 y extrae el tercer 
#renglón y la segunda columna.
M6 <- matrix(sample(20:50, 25), nrow = 5, ncol = 5)
M6_r3 <- M6[3, ]
M6_c2 <- M6[, 2]
M6_r3c2 <- cbind(M6_r3, M6_c2)
M6_r3c2  #algo así 
#también así...
M6_r3c2_1 <- M6[3, 2] #más bien esto era lo que se estaba pidiendo
M6_r3c2_1

# Ejercicio 11. Matriz génica con 6 genes y cuatro condiciones
expresion_genica <- matrix(rnorm(1:24), nrow = 6, ncol = 4)
expresion_genica
nombres_genes <- c("B-actin", "AQP1", "GADPH", "BCRA1", "P53", "TNF")
condiciones <- c("Control blanco", "Control positivo", "Control negativo", "Tratamiento")
colnames(expresion_genica) <-condiciones
rownames(expresion_genica) <- nombres_genes
expresion_genica
#promedio de expresión de cada gen 
B_actin_promedio <- mean(expresion_genica[1, ])
AQP1_promedio <- mean(expresion_genica[2, ])
GADPH_promedio <- mean(expresion_genica[3, ])
BCRA1_promedio <- mean(expresion_genica[4, ])
P53_promedio <- mean(expresion_genica[5, ])
TNF_promedio <- mean(expresion_genica[6, ])

mean(expresion_genica[1:6, ])

promedio <- c(mean(expresion_genica[1, ]), mean(expresion_genica[2, ]), mean(expresion_genica[3, ]),
              mean(expresion_genica[4, ]), mean(expresion_genica[5, ]),mean(expresion_genica[6, ])
              )
promedio
apply(expresion_genica, 1, mean)


#Ejercicio 12 Red de interacciones proteína-proteína
#Modela una matriz de interacciones entre proteínas donde 1 indica interacción 
#y 0 indica no interacción.
matriz_interaccion <- matrix(sample(0:1, replace = TRUE, 25), nrow = 5, ncol = 5)
matriz_interaccion
nombres_proteinas <- c("Proteina 1", "Proteina 2", "Proteina 3", "Proteina 4", "Proteina 5")
colnames(matriz_interaccion) <-nombres_proteinas
rownames(matriz_interaccion) <- nombres_proteinas
interaccion_total_P1 <- sum(matriz_interaccion[1, ]); interaccion_total_P1
interaccion_total_P2 <- sum(matriz_interaccion[2, ]); interaccion_total_P2
interaccion_total_P3 <- sum(matriz_interaccion[3, ]); interaccion_total_P3
interaccion_total_P4 <- sum(matriz_interaccion[4, ]); interaccion_total_P4
interaccion_total_P5 <- sum(matriz_interaccion[5, ]); interaccion_total_P5

#Ejercicio 13. Supongamos que tienes datos de concentraciones de 4 metabolitos 
#en 3 tipos de tejidos diferentes. Crea una matriz concentraciones de 4x3
#con datos aleatorios. Asigna nombres de metabolitos a las filas y tipos de 
#tejidos a las columnas. Normaliza las concentraciones para cada metabolito 
#(dividiendo por el máximo valor de cada fila).
matriz_concentracion <- matrix(rnorm(1:12), nrow = 4, ncol = 3)
matriz_concentracion
nombres_metabolitos <- c("Metabolito 1", "Metabolito 2", "Metabolito 3", "Metabolito 4")
nombres_tejidos <- c("Tejido 1", "Tejido 2", "Tejido 3")
colnames(matriz_concentracion) <- nombres_tejidos
rownames(matriz_concentracion) <- nombres_metabolitos
max(matriz_concentracion)
matriz_concentracion_normalizada <- matriz_concentracion/max(matriz_concentracion)
matriz_concentracion_normalizada 
