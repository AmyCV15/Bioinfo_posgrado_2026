###########
##indice de diversidad de shannon
#calcula diveridad alfa -- que tan equitativo es en terminos de abundancias 
abundancias <- c(5, 5, 5, 5, 250)
probabilidad <- abundancias/sum((abundancias))
shannnon <- -sum(probabilidad*log(probabilidad))
shannnon
#logaritmo de la riqueza es el numero/valor maximo que se puede obtener en el indice de shannon
log(5)
#version para pielow -- valor normalizado a 0-1
-sum(probabilidad*log(probabilidad))/log(length(abundancias))

##para siguiente clase 
BiocManager::install("dada2", version = "3.22") #no funcionó
devtools::install_github("benjjneb/dada2", ref="v1.16")


if(!requireNamespace("BiocManager")){
  install.packages("BiocManager")
}
BiocManager::install("phyloseq")

BiocManager::install("dada2")
BiocManager::install("phyloseq")
BiocManager::install("microbiome")

#indice de simpsom
#la probabilidad de que al tomar dos individuos al azar. sean de la misma especie
#lo que mide realemte es dominancia. Que tan cercano a 1 es, qué tan dominante es una especie. 

#curava de rank abundances 


##Diversidad beta:
#que mide?
#diferencias en composiicion de especies 
#recambio y anidamiento de especies 
#dos familias de indices para la diversidad beta: diferencias de especies y diferenciacion de abundancias
#indice de jaccard: que tan similares son tood los sitios. si la distancia es 1, son identicos los sitios
#si es de 0, son completamente distintos
#sorecen dice
#es una distancia entre dos puntos para expresar que tan diferentes son.


#para trabajar con DADA2 vamos a crear un nuevo script.