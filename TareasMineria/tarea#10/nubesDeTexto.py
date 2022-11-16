from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

textoGeneros = ""
textoDesarrollador=""

# leo el dataframe
cd = pd.read_csv("datosJuegoLimpio.csv")


# guardamos el texto de todas las filas en un archivo txt
def filtrarGenero(renglon):
    global textoGeneros
    textoGeneros += renglon
def filtrarDesarollador(renglon):
    global textoDesarrollador
    textoDesarrollador += str(renglon+" ")

cd["desarrollador"].apply(filtrarDesarollador)
cd["genero"].apply(filtrarGenero)

archivo = open("GenerosDeVideojuegos.txt", mode="w")
archivo.write(textoGeneros)
archivo.close()
archivo = open("DesarolladoresDeVideojuegos.txt", mode="w")
archivo.write(textoDesarrollador)
archivo.close()


# Recupero el texto
archivo = open("GenerosDeVideojuegos.txt", mode="r")
textoGeneros = archivo.read()
archivo.close()
archivo = open("DesarolladoresDeVideojuegos.txt", mode="r")
textoDesarrollador = archivo.read()
archivo.close()


# Muestro y guardo el imagen de la nube de texto

# Para los generos 
mascaraGen = np.array(Image.open("Megaman.png"))
nubeGen = WordCloud(max_words=1000, mask=mascaraGen, margin=10,random_state=1).generate(textoGeneros)
default_colors = nubeGen.to_array()
plt.figure()
plt.axis("off")
plt.title("NUBE DE LOS GENEROS DE VIDEOJUEGOS")
plt.imshow(default_colors, interpolation="bilinear")
#plt.show()
nubeGen.to_file("MegaNube_Generos.png")

# Para los desarrolladores
mascaraDes = np.array(Image.open("AmongUs.png"))
nubeDes = WordCloud(max_words=2000, mask=mascaraDes,margin=10, random_state=1).generate(textoDesarrollador)
default_colors = nubeDes.to_array()
plt.figure()
plt.axis("off")
plt.title("NUBE DE LOS DESARROLLADORES DE VIDEOJUEGOS")
plt.imshow(default_colors, interpolation="bilinear")
#plt.show()
nubeDes.to_file("AmongUsNube_Desarrolladores.png")


