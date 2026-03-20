######
### Clase de 05 de marzo 2026 ######
# IF
#Ejercicio 1. 
#Elabora un programa que compare tu estatura con tu ídolx y determine si eres más altx.
mi_estatura <- 1.90
estatura_idolo <- 1.80

if(mi_estatura > estatura_idolo) {
  print("Eres más alto que tu ídolo")
} 

##Ejercicios
mole <- "si"
pozole <- "no"
if(mole == "si" & pozole == "si"){
  print("Te gusta el mole y el pozole")
} else{
  print("No te gusta una de las opciones")
}

#ahora con or
if(mole == "si" | pozole== "si"){
  print("te gusta una de las opciones")
}

#fechas de cumpleaños 
mes_cumpleaños <- "Marzo"
if( mes_cumpleaños == "Enero" | mes_cumpleaños== "Febrero" | mes_cumpleaños== "Diciembre"){
  print("Naciste en invierno")
} else if(mes_cumpleaños == "Marzo" | mes_cumpleaños =="Abril" | mes_cumpleaños =="Mayo"){
  print("Naciste en primavera")
} else if ( mes_cumpleaños == "Junio" | "Julio" | "Agosto"){
  print("Naciste en verano")
} else {
  print("Naciste en otoño")
}

#Dado un valor de pH de una muestra, escribe un código en R que determine si el ambiente es ácido 
#( pH<  7) o neutro (   p  H =    7).
ph <- 9
if (ph < 7){
  print("el pH es acido")
} else if (ph > 7){
  print("el pH es básico")
}

#### clase de  12 de marzo 2026 ###
#capitulo 9 de notas de r




#### python ###
install.packages("reticulate")
library(reticulate)
