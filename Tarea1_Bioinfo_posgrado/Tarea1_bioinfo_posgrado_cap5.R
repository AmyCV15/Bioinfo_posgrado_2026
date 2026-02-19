###############
### Ejercicios capitulo 5 ###
# E1. Datos de crecimiento bacteriano. 10 cepas en 3 medios diferentes 
#a 4 temperaturas diferentes... esto da 120 combinaciones! Para agilizar esto,
#se buscará una función que nos ayude
cepas <- paste("cepa", 1:10)
medios <- c("Medio A", "Medio B", "Medio C")
temperaturas <- c(37, 37.5, 28.5, 29)
#funcion que nos ayuda a generar lac combinaciones:
cepa_temp_med <- expand.grid(Cepa = cepas, 
            Medio = medios, 
            Temperatura = temperaturas)
cepa_temp_med
as.data.frame(cepa_temp_med)
#agregando coumna de tasa de crecimiento con num aleatorios:
cepa_temp_med$tasa_crecimiento <- rnorm(1:120)
cepa_temp_med
#promedio tasa de crecimiento por cada medio
#forma tardada:
medioA <- cepa_temp_med[cepa_temp_med$Medio == "Medio A", c(2, 4)]
medioA
mean(medioA$tasa_crecimiento); sd(medioA$tasa_crecimiento)
medioB <- cepa_temp_med[cepa_temp_med$Medio == "Medio B", c(2, 4)]
medioB
mean(medioB$tasa_crecimiento); sd(medioB$tasa_crecimiento)
medioC <- cepa_temp_med[cepa_temp_med$Medio == "Medio C", c(2, 4)]
medioC
mean(medioC$tasa_crecimiento); sd(medioC$tasa_crecimiento)
 #alguna forma mejor?

# E2. data frame de resitencia con: Cepa, Antibiótico, Resistencia 
#(0 para sensible, 1 para resistente).

resistencias <- data.frame(
  cepas = c("Cepa 1", "Cepa 2", "Cepa 3", "Cepa 4", "Cepa 5"),
  antibiotico = rep(1:5, each =5),
  resistencia = sample(0:1, 25, replace = TRUE)
)

#otra forma de hacer lo de las cepas es : paste("cepa", 1:10)
resistencias

#calcula el porcentaje de resitencias para cada antibiotico
(sum(resistencias[resistencias$antibiotico == 1, 3]) * 100) / 5 #y así para cada uno
##buscar una forma más agilizada
 
