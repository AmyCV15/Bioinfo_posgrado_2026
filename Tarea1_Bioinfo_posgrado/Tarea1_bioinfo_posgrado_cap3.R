####### Tarea 1: Bioinfo posgrado#### 
#### Ejercicios del capítulo 3 ###

#####1. Dado un vector x, escribe un código que determine si todos los elementos del 
#vector son iguales a cero utilizando la función all().

#creando vector 
X <- c(1:10)
X
all(X == 0)
#resultado: FALSE

#####2. Escribe un código que tome un vector x y devuelva TRUE si hay algún 
#elemento repetido en el vector, utilizando la función any().
X <- rep(X, 2)
X
any(X == X) #resultado: TRUE

#####3. Dado un vector x, escribe una función que determine si todos los elementos del 
#vector son iguales entre sí utilizando la función all().
print(X[11]) #esta línea imprime el valor asignado en la posición 11 de mi vector X.

all(X[1] == X) #si todos los valores son iguales al primero, entonces, todos 
#son iguales entre sí. Para este caso, no lo son. 

##### 4. Escribe una función que tome dos vectores (“x” y “y”) y devuelva TRUE 
#si ambos vectores tienen algún elemento en común, utilizando la función any()
Y <- c(10:19); Y <- rep(Y, 2)


##### 5. Escribe una función que tome dos vectores (“x” y “y”) y devuelva TRUE si 
#todos los elementos del vector x son mayores que los elementos correspondientes 
#en el vector y, utilizando la función all().
all( X > Y) #Falso debido a los valores que yo asigné a mis vectores. 
#modificando valores 
X <- X*11
X
all( X > Y) #ahora sí, el resultado es verdadero. 

#####6 . Dado un vector x, escribe una función que determine si todos los elementos del 
#vector son menores que cero utilizando la función all().
all(X < 0)

##### 7. Escribe una función que tome dos vectores (“x” y “y”) y devuelva TRUE 
#si al menos un elemento del vector x es mayor que los elementos correspondientes 
#en el vector y, utilizando la función any().
any(X > Y) #TRUE

##### 8. Dado un vector x, escribe una función que determine si todos los 
#elementos del vector son iguales a un valor específico a utilizando la 
#función all().
all(X == 2) #FALSE dado que los valores del vector, aunque se repiten, ninguno es 2 y
#el vector no está compuesto únicamente por el valor "2" repetido.
all(X == "Hola")  #ningun valor del vector es de texto.

##### 9. Escribe una función que tome dos vectores (“x” y “y”) y devuelva TRUE 
#si al menos un elemento del vector x es menor que los elementos correspondientes 
#en el vector y, utilizando la función any().
X <- X/10 #para que el resultado del ejercicio sea TRUE
X
any(X < Y)

##### Operaciones con vectores ####
##### 10. ¿qué función tienen los siguientes comandos?
help(sd) #calcula la desviación estándar de un conjunto de datos dado un vector X.
help(quantile) #calcula quantiles de un vector dado x dependiendo de la 
#probabilidad que se le asinge.

##### 11. ¿Cuál es el promedio de las edades sin contar la de Beth? 
#copiando comandos para generar data frame de "EDADES"
edades <- c(35,35,70,17,14) 
nombres <- c("Jerry","Beth","Rick", "Summer","Morty")
names(edades) <- nombres 
edades #se copió todo de manera correcta.
mean(edades[-2]) #no funciona si usamos el nombre "Beth" en lugar de su 
#posición en el vector

##### 12. Quiten a Morty del vector, ordénenlo y guárdenlo como un nuevo objeto.
Morty <- edades[5]
Morty
edades_sMorty <- edades[-5]
edades_sMorty
##### 12. ¿Hay alguna edad que sea mayor de 75? ¿Menor de 12? ¿Entre 12 y 20?
any(edades > 60)
any(edades < 12)
any(edades >= 12); any(edades <= 20)

###### Tamaños de genomas ####
#13. Generar vector de edades de 10 compañeros, asígnales nombre.
edades_compañeros <- seq(from = 21, to = 30, by= 1)
edades_compañeros <- sample(edades_compañeros, replace = TRUE)
nombres_compñeros <- c("Amairani", "Itzel", "Vanessa", "Eliseo", "Melanie", "CLaudia",  
                       "Carolina", "Diana", "Eren", "Bernardo")
names(edades_compañeros) <- nombres_compñeros 
edades_compañeros
# Encuentra el mínimo,máximo, media, mediana, la desviación estándar, la 
#longitud del vector y selecciona sólo los elementos impares.
range(edades_compañeros)
mean(edades_compañeros)
median(edades_compañeros)
sd(edades_compañeros)
length(edades_compañeros)
edades_compañeros_orden <- sort(edades_compañeros)
edades_compañeros_orden
#
any(edades_compañeros == edades_compañeros)
which(edades_compañeros == edades_compañeros)
#
#evidentemente esto no me está dando lo que necesito porque la lógica con la
#cual funcionan es diferente.
edades_impar <- edades_compañeros[edades_compañeros %% 2 != 0]
edades_impar
# lo que hace el paso anterior es dividir cada componente del vector en 2, 
#si el residuo de la división es 0, significa que el número puede divirse en dos sin problema 
#(sin numeros decimales), por lo que es número par. Si el residuo de la división es mayor a 0,
#quiere decir que no es un numero par. Esto lo investigué en la red, cabe aclarar.


# Elimina el máximo y el mínimo y con el vector resultante realiza un histograma.
edades_compañeros <- sort(edades_compañeros)
edades_compañeros_hist<- edades_compañeros[-c(1, 10)] 
edades_compañeros_hist
hist(edades_compañeros_hist)
# Crea un vector de caracteres con diez nombres de especies y asocialo con su 
#número de acceso de NCBI para su genoma en nucleótidos.
especies_AccNum_nombres <- c("Saccharomyces cerevisiae", "Escherichia coli", "Pseduomonas aeruginosa", "Candida albicans", 
                     "Proteus mirabilis", "Saccharomyces pastorianus", "Candida tropiccalis", "Mycobacterium tuberculosis",
                     "Streptococcus pneumoniae", "Gardnerella vaginalis")
especies_AccNum <- c("GCA_000146045.2", "GCA_000008865.2", "GCA_000006765.1", "GCA_000182965.3", "GCA_000069965.1", 
                     "GCA_011022315.1", "GCA_000006335.3", "GCA_000195955.2", "GCA_001457635.1", "GCA_001042655.1")
names(especies_AccNum) <- especies_AccNum_nombres
especies_AccNum

###### 14. Crea un vector con los meses en los que todas las alumnas del grupo 
#cumplen años. 3. Aprovecha los levels para generar un objeto que guarde el 
#número de estudiantes que cumplen años cada mes.
meses_cumpleaños <- c("Febrero", "Marzo", "Abril", "Abril", "Junio", "Julio", "Marzo", "Septiembre", "Octubre", 
          "Noviembre", "Octubre")
as.factor(meses_cumpleaños)
numero_estudiantes_cada_mes <- table(meses_cumpleaños)
numero_estudiantes_cada_mes

##### 15. 
virus_nombres <- c("Influenza A", "Influenza B", "Norovirus", "VPH", "Varicela-Zoster", "Herpes simple",
                   "Rotavirus", "VSR", "Epstein Barr", "Adenovirus")
acc_num <- c("GCA_000865725.1", "GCA_000820495.2", "GCA_000864005.1", "GCA_001274345.1", "GCA_000858285.1", 
             "GCA_000859985.2", "GCA_000880735.1", "GCA_964661075.1", "GCA_002402265.1", "GCA_025630205.1	")
tamaño_genomas <- c(13600, 14500, 7700, 7300, 124900, 152200, 18600, 15200, 171800, 36000)

names(acc_num) <- virus_nombres
acc_num
names(tamaño_genomas) <- virus_nombres 
tamaño_genomas
tamaño_genomas[which(tamaño_genomas > 300)]
#lo haré con mayores y menores a 8000 para que no sea un vector vacío
menores <- tamaño_genomas[which(tamaño_genomas < 8000)]
menores
mayores <- tamaño_genomas[which(tamaño_genomas  > 8000)]
mayores
hist(tamaño_genomas)
boxplot(tamaño_genomas) #así me genera una sola caja, puesto que es únicamente
                        #un cojunto de datos y realiza los cálculos con ese conjunto de datos.
boxplot(tamaño_genomas ~ virus_nombres) #utilizando la fórmula de esta manera
                                        #ya me muestra todos los virus diferentes,
                                        #pero no puede hacer los cálculos 
                                        #que se representan en un boxplot
                                     
