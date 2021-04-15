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
    print("5- Buscar videos con mas likes con un tag y pais especifico")
    print("6- Buscar videos con mas likes para una categoria")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga la informacion de los videos en la estructura de datos
    """
    return controller.loadData(catalog)
def topVideos(catalog, topAmount, country, category):
    return controller.topVideos(catalog, topAmount, country, category)

def trendingCountry(catalog, country):
    return controller.trendingCountry(catalog, country)

def trendingCategory(catalog, category):
    return controller.trendingCategory(catalog, category)


def mostLiked(catalog, tag, number, country):
    return controller.mostLiked(catalog, tag, number, country)

def mostLikedCategories(catalog, number, category):
    return controller.mostLikedCategories(catalog, number, category)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ......")
        catalog = initCatalog()
        answer= loadData(catalog)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories']))) 
    elif int(inputs[0]) == 2:
        countryname= input("Ingrese el pais del que desea consultar el top: ")
        topAmount= int(input("Escoga la cantidad de videos que desea ver en el top: "))
        category= input("Ingrese la categoria de los videos: ")
        print("Cargando el top de los videos")
        answer= topVideos(catalog,topAmount,countryname,category)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 3:
        country= input("Ingrese el pais que desea consultar : ")
        print("El video mas trending en este pais es: ")
        answer=trendingCountry(catalog, country)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 4:
        category= input("Ingrese la categoria que desea consultar : ")
        print("El video mas trending en esta categoria es: ")
        answer=trendingCategory(catalog, category)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 5:
        tag= input("Ingrese el tag que desea consultar : ")
        country= input("Ingrese el pais que desea consultar : ")
        number= int(input("Ingrese la cantidad de videos que desea consultar : "))
        print("Cargando los videos con mas likes que tienen este tag...")
        answer= mostLiked(catalog, tag, number, country)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
                "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 6:
        number= int(input("Ingrese la cantidad de videos que desea consultar : "))
        category= input("Ingrese la categoria que desea consultar : ")
        print("Cargando los videos con mas likes de la categoria seleccionada...")
        answer= mostLikedCategories(catalog, number, category) 
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")      
    else:
        sys.exit(0)
sys.exit(0)
