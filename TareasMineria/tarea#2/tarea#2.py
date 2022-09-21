# PROBANDO COMANDOS EN EL CONJUNTO DE DATOS ESCOGIDO EN LA TAREA #1

# Libreria necesarias
import pandas
from datetime import datetime

print("----------------------------------------------------- IMPORTACION DE LOS DATOS -----------------------------------------------------")

print("\nCOMANDO -> pandas.read_csv()")
# Lee el conjunto de datos
conjuntoDeDatos = pandas.read_csv("datosJuegos.csv")
# Imprime todos los datos, todas las columnas
print(conjuntoDeDatos)


print("\nCOMANDO -> pandas.date_range()")
# Imprime los dias que hay entre dos fechas
print(pandas.date_range("2017-01-01", "2017-02-01"))
# Imprime los 10 dias siguientes al de la fecha inicial
print(pandas.date_range("2017-01-01", periods=10))


print("\n\n\n---------------------------------------------------------- DATA CLEANING -----------------------------------------------------")
print("\nAntes del [dropna] filas = 17944     despues del [dropna] filas = 17922")
print(conjuntoDeDatos.dropna())

# rellena los valores nulos con un valor deseado
print("\nCOMANDO -> conjuntoDeDatos.fillna()")
print(conjuntoDeDatos.fillna("0"))

# Ordena los datos en base a la fecha de estreno, de las recien a la mas antigua
print("\nCOMANDO -> conjuntoDeDatos.sort_values()")
print(conjuntoDeDatos.sort_values("r-date"))

print("\nCOMANDO -> conjuntoDeDatos.groupby()")
print(conjuntoDeDatos.groupby("platform"))

# Renombro todos los encabezados de las columnas
print("\nCOMANDO -> conjuntoDeDatos.columns = []")
conjuntoDeDatos.columns=["nombre", "plataforma", "fecha lanzamiento", "puntuacion", "puntuacion usuarios", "desarrollador", "genero", "numero jugadores", "numero criticas", "numero usuarios"]

# Reemplazo el indice por el nombre de los juegos
print("\nCOMANDO -> conjuntoDeDatos.set_index()")
conjuntoDeDatos.set_index("nombre", inplace=True)

print("\nCOMANDO -> conjuntoDeDatos.to_csv()")
conjuntoDeDatos.to_csv("datosJuegoLimpio.csv")


print("\n\n\n----------------------------------------------------- ESTADISTICAS DE LOS DATOS --------------------------------------------")

# Imprime los 15 primeros datos, todas las columnas
print("\nCOMANDO -> conjuntoDeDatos.head(15)")
print(conjuntoDeDatos.head(15))
# Imprime los 15 ultimos datos, todas las columnas
print("\nCOMANDO -> conjuntoDeDatos.tail(15)")
print(conjuntoDeDatos.tail(15))
# Informacion del dataframe
print("\nCOMANDO -> conjuntoDeDatos.info()")
print(conjuntoDeDatos.info())
# Obtiene datos estadisticos 
print("\nCOMANDO -> conjuntoDeDatos.describe()")
print(conjuntoDeDatos.describe())
# Obtiene la media de todas las columnas numericas
print("\nCOMANDO -> conjuntoDeDatos.mean(numeric_only=True)")
print(conjuntoDeDatos.mean(numeric_only=True))
# Obtiene el valor medio de todas las columnas numericas
print("\nCOMANDO -> conjuntoDeDatos.median(numeric_only=True)")
print(conjuntoDeDatos.median(numeric_only=True))
# Obtinene la desviacion estandar
print("\nCOMANDO -> conjuntoDeDatos.std(numeric_only=True)")
print(conjuntoDeDatos.std(numeric_only=True))
# Obtinene una matriz de correlacion 
print("\nCOMANDO -> conjuntoDeDatos.corr()")
print(conjuntoDeDatos.corr())
# Cuenta todos los valores diferentes Nan
print("\nCOMANDO -> conjuntoDeDatos.count(numeric_only=True)")
print(conjuntoDeDatos.count(numeric_only=True))
# Obtinene el valor maximo 
print("\nCOMANDO -> conjuntoDeDatos.max(axis=0, numeric_only=True)")
print(conjuntoDeDatos.max(axis=0, numeric_only=True))
# Obtinene el valor minimo
print("\nCOMANDO -> conjuntoDeDatos.min(axis=0, numeric_only=True)")
print(conjuntoDeDatos.min(axis=0, numeric_only=True))
