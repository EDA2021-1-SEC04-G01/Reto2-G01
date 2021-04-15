﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import time
import tracemalloc 



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    tracemalloc.start() 
    delta_time = -1.0 
    delta_memory = -1.0

    start_time = getTime() 
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategories(catalog)

    stop_time = getTime() 
    stop_memory = getMemory()
    tracemalloc.stop()
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory
    

def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category)


# Funciones de toma de tiempo y memoria
def getTime(): 
    """ 
    devuelve el instante tiempo de procesamiento en milisegundos
     """
    return float(time.perf_counter()*1000)

def getMemory(): 
    """ 
    toma una muestra de la memoria alocada en instante de tiempo 
    """ 
    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory): 
    """ 
    calcula la diferencia en memoria alocada del programa entre dos 
    instantes de tiempo y devuelve el resultado en kBytes (ej.: 2100.0 kB) 
    """ 
    memory_diff = stop_memory.compare_to(start_memory, "filename") 
    delta_memory = 0.0 
 
    for stat in memory_diff: 
        delta_memory = delta_memory + stat.size_diff
    delta_memory = delta_memory/1024.0 
    return delta_memory

# Funciones de consulta sobre el catálogo
def topVideos(catalog, topAmount, countryname, category):
    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    model.topVideos(catalog, topAmount, countryname, category)
   

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

def trendingCountry(catalog, country):
    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    model.trendingCountry(catalog, country)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory
  
def trendingCategory(catalog, category):
    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    model.trendingCategory(catalog, category)


    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory
 
def mostLiked(catalog, tag, number, country):
    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    model.mostLiked(catalog, tag, number, country)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

def mostLikedCategories(catalog, number, category):
     
     delta_time = -1.0
     delta_memory = -1.0

     tracemalloc.start()
     start_time = getTime()
     start_memory = getMemory()

     model.mostLikedCategories(catalog, number, category)


     stop_memory = getMemory()
     stop_time = getTime()
     tracemalloc.stop()

     delta_time = stop_time - start_time
     delta_memory = deltaMemory(start_memory, stop_memory)
     return delta_time, delta_memory
    

    
