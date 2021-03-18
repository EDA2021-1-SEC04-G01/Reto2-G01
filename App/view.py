"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt # pylint: disable=import-error
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar Top x de videos mas vistos en un pais en una categoria")
    print("3- Buscar video con mas dias en trending por pais")
    print("4- Buscar video con mas dias en trending por categoria")
    print("5- Buscar videos con mas likes con un tag especifico")
    print("5- Buscar videos con mas likes para una categoria")
    print("0- Salir")

def initCatalog(dtEstructure):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(dtEstructure)


def loadData(catalog, dtEstructure):
    """
    Carga la informacion de los videos en la estructura de datos
    """
    controller.loadData(catalog, dtEstructure)
def topVideos(catalog, topAmount, country, category,sorting):
    controller.topVideos(catalog, topAmount, country, category,sorting)

def trendingCountry(catalog, country):
    controller.trendingCountry(catalog, country)

def trendingCategory(catalog, category):
    controller.trendingCategory(catalog, category)


def mostLiked(catalog, tag, number, country):
    controller.mostLiked(catalog, tag, number, country)

def mostLikedCategories(catalog, number, category):
    controller.mostLikedCategories(catalog, number, category)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Seleccione la estructura de datos que deseea escoger: ")
        dt= int(input("Para Array escriba 0, Para Single-Linked escriba 1: "))
        if dt == 0:
            dtEstructure='ARRAY_LIST'
        else:
             dtEstructure="SINGLE_LINKED"
        print("Cargando información de los archivos ......")
        catalog = initCatalog(dtEstructure)
        loadData(catalog, dtEstructure)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories']))) 
    elif int(inputs[0]) == 2:
        print("Seleccione el tipo de algoritmo de ordenamiento\n Shell= 0\n Insertion = 1\n Selection = 2\n Merge = 3\n Quick = 4")
        sorting = int(input("Ingrese el numero: "))
        countryname= input("Ingrese el pais del que desea consultar el top: ")
        topAmount= int(input("Escoga la cantidad de videos que desea ver en el top: "))
        category= input("Ingrese la categoria de los videos: ")
        start_time = time.process_time()
        print("Cargando el top de los videos")
        print(topVideos(catalog,topAmount,countryname,category,sorting))
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("El tiempo [ms] es: "+str(elapsed_time_mseg))
    elif int(inputs[0]) == 3:
        country= input("Ingrese el pais que desea consultar : ")
        print("El video mas trending en este pais es: ")
        trendingCountry(catalog, country)      
    elif int(inputs[0]) == 4:
        category= input("Ingrese la categoria que desea consultar : ")
        print("El video mas trending en esta categoria es: ")
        trendingCategory(catalog, category)
    elif int(inputs[0]) == 5:
        tag= input("Ingrese el tag que desea consultar : ")
        country= input("Ingrese el pais que desea consultar : ")
        number= int(input("Ingrese la cantidad de videos que desea consultar : "))
        print("Cargando los videos con mas likes que tienen este tag...")
        mostLiked(catalog, tag, number, country)

    elif int(inputs[0]) == 6:
        number= int(input("Ingrese la cantidad de videos que desea consultar : "))
        category= input("Ingrese la categoria que desea consultar : ")
        print("Cargando los videos con mas likes de la categoria seleccionada...")
        mostLikedCategories(catalog, number, category)       
    else:
        sys.exit(0)
sys.exit(0)
