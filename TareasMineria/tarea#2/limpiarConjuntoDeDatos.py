# PROBANDO COMANDOS EN EL CONJUNTO DE DATOS ESCOGIDO EN LA TAREA #1

# Libreria necesarias
import pandas
from datetime import datetime

def formatoFechas(fecha):
    fechaSeparada = fecha.split()
    tem = ""
    if(fechaSeparada[0] == "January"):
        fechaSeparada[0] = "01"
    elif(fechaSeparada[0] == "February"):
        fechaSeparada[0] = "02"
    elif(fechaSeparada[0] == "March"):
        fechaSeparada[0] = "03"
    elif(fechaSeparada[0] == "April"):
        fechaSeparada[0] = "04"
    elif(fechaSeparada[0] == "May"):
        fechaSeparada[0] = "05"
    elif(fechaSeparada[0] == "June"):
        fechaSeparada[0] = "06"
    elif(fechaSeparada[0] == "July"):
        fechaSeparada[0] = "07"
    elif(fechaSeparada[0] == "August"):
        fechaSeparada[0] = "08"
    elif(fechaSeparada[0] == "September"):
        fechaSeparada[0] = "09"
    elif(fechaSeparada[0] == "October"):
        fechaSeparada[0] = "10"
    elif(fechaSeparada[0] == "November"):
        fechaSeparada[0] = "11"
    elif(fechaSeparada[0] == "December"):
        fechaSeparada[0] = "12"
    for i in range(len(fechaSeparada[1])-1):
        tem += fechaSeparada[1][i]
    fechaSeparada[1] = tem
    fechaFormateada = str(fechaSeparada[1]+"/"+fechaSeparada[0]+"/"+fechaSeparada[2])
    return datetime.strptime(str(fechaFormateada),"%d/%m/%Y")
def limpiarTBD(valor):
    if str(valor) == "tbd":
        return 0.0
    else :
        return valor 
print("----------------------------------------------------- IMPORTACION DE LOS DATOS -----------------------------------------------------")

print("\nCOMANDO -> pandas.read_csv()")
# Lee el conjunto de datos
conjuntoDeDatos = pandas.read_csv("datosJuegos.csv")

conjuntoDeDatos.dropna()

# rellena los valores nulos con un valor deseado
conjuntoDeDatos.fillna("0")

# Renombro todos los encabezados de las columnas
conjuntoDeDatos.columns=["nombre", "plataforma", "fecha lanzamiento", "puntuacion", "puntuacion usuarios", "desarrollador", "genero", "numero jugadores", "numero criticas", "numero usuarios"]

# convierto la fecha a un formato que python entienda
conjuntoDeDatos["fecha lanzamiento"] = conjuntoDeDatos["fecha lanzamiento"].map(formatoFechas)
conjuntoDeDatos.sort_values(by="fecha lanzamiento", inplace=True)
conjuntoDeDatos["puntuacion usuarios"] = conjuntoDeDatos["puntuacion usuarios"].map(limpiarTBD)
#df.sort_values(by='Date of Birth', inplace=True)
print(conjuntoDeDatos)

print("\nCOMANDO -> conjuntoDeDatos.to_csv()")
conjuntoDeDatos.to_csv("datosJuegoLimpio.csv")


