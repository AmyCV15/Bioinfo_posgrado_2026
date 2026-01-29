#Clase 1 bioinfo 29 de enero
datos <- rnorm(1:1000)

pdf("03_results/mi_histograma.pdf")
hist(datos, col = "blue")
dev.off() #esta linea es para que ya no imprima más adelante las siguientes figuras
#que yo vaya generando y guardando en PDF
tiff("03_results/mi_histograma.tiff")
hist(datos, col = "pink")
dev.off()

#después de descargar git, se abre un nuevo proyecto en version control y pegar el 
#link del repositorio de github

#para poder enlazar R con github "de aquí hacia allá":
install.packages("usethis")
usethis::use_git()
usethis::create_github_token()
gitcreds::gitcreds_set()
usethis::use_git_config(
  user.name = "AmyCV15",
  user.email = "chavezamairani@gmail.com"
)
usethis::use_github()
