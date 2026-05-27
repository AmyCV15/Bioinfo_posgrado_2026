#### Bioconductor ####

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.22")

BiocManager::install("Biostrings")

#########################################################################
primer <-DNAString("GACCCGCTCGGACTTACT")
primers_juntos <- DNAStringSet(c("GACCCGCTCGGACTTACT", "CTTCTGGACCCATGCTGT", "CAGCCCAAGGACAGTTCAGAG", 
                                 "CCATCATGGCTAAGTGCACAG", "ATGM"))
primer[1:3]
primers_juntos[[1]][1:3]
#IUPAC CODE MAP para conocer el alfabeto extendido
#para poner nombres a las secuencias
names(primers_juntos) <- c("AQP1_F", "AQP1_R", "DNA2", "DNA3")
primers_juntos
width(primers_juntos) #me regresa un vector indicando el tamaño de cada secuencia
rev(primers_juntos)
rev(primer)#cambia al inverso (orden)
translate(primer)
translate(primers_juntos[1:4])
reverseComplement(primer)
alphabetFrequency(primer) #cantidad de letras en la secuencia
letterFrequency(primer, "A")
dinucleotideFrequency(primer)
library(BSgenome)
install.packages("BSgenome")



### Clase del 23 de abril de 2026 ###
#Cambios en la expresión génica. Fold change: cambio relativo C/R
#ventajas: dice cuánto cambió. Desventajas: no tener el signo para explicar si el cambio fue 
#de auemnto o disminución. Si es mayor a 1, aumenta, si es menor, disminuye.
# Log fold change <- forma de regresar a los signos.
#Se calcula el logartimo BASE 2 del fold change.
#log2 de 2 = 1. Se duplicó.
#log2 de 4 = 2. Se cuadrruplicó
#logaritmo de un numero entre 0 y 1 siemore es negativo.
log(0.5, 2)
#en las volcano plot el eje de las y no signfica el valor de p, sino menos el logaritmo del valor de p
#para que los valores significativos queden arriba y no abajo, solo por conveniencia para la vista.
#los genes 


#cargando archivo fasta
library(Biostrings)
globinas <- readAAStringSet("01_RawData/globinas.fasta")
HIV <- readDNAStringSet("01_RawData/NC_001802_HIV-1.fasta")
#cua es la frecuencia de cada aminoacido en todas las secuencias 
alphabetFrequency(globinas) #NOTA: el punto es un codón de paro, el más es una inserción y el menos una deleción.

#ejercicios de clase
#Ejercicio 1. Creación y manipulación de secuencias 
sec1 <-DNAString("AGTCGTAGC")
#Encuentra el complemento inverso de la secuencia.
reverseComplement(sec1)
#encuentra las ocurrencias del nucleotido "A"
letterFrequency(sec1, letters="A")
#Extrae la subsecuencia de la posición 3 a la 7
sec1[3:7]

#Ejercicio 2. Coincidencia de patrones
sec2 <- DNAString("AGTCAGCTAG")
#Encuentra todas las coincidencias exactas del patrón “AGC”.
matchPattern("AGC", sec2)
#Realiza coincidencias aproximadas del patrón “AGC” permitiendo 1 desajuste

matchPattern("AGC", sec2, max.mismatch = 1)
vmatchPattern("AGC", HIV, max.mismatch = 1) #vmatchPattern cuando se tiene string tipo set

#Ejercicio 3. Alineación de secuencias
#Realiza una alineación global entre las secuencias “ACGT” y “AGCT”.
pairwiseAlignment(DNAString("ACGT"), DNAString("AGCT"), type="global") # no se puede
BiocManager::install("pwalign")
library(pwalign)
pairwiseAlignment(DNAString("ACGT"), DNAString("AGCT"), type="global") #ahora sí 
pairwiseAlignment(DNAString("ACGT"), DNAString("AGCT"), type="local")
######################################
##Instalando sleuth
source("http://bioconductor.org/biocLite.R")
biocLite("rhdf5")
install.packages('rhdf5')
install.packages('Rtools')
install("rhdf5")
install.packages("devtools")
devtools::install_github("pachterlab/sleuth")



if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install()
BiocManager::install("devtools")    # only if devtools not yet installed
BiocManager::install("pachterlab/sleuth")

install.packages(c("fs", "curl", "glue", "processx"))
