"""
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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(dtEstructure):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(dtEstructure)
    return catalog

# Funciones para la carga de datos
def loadData(catalog, dtEstructure):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog, dtEstructure)
    loadCategories(catalog)
    

def loadVideos(catalog, dtEstructure):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video, dtEstructure)

def loadCategories(catalog):
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category)

def mostLikedCategories(catalog, number, category):
    model.mostLikedCategories(catalog, number, category)


# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def topVideos(catalog, topAmount, countryname, category,sorting):
    return model.topVideos(catalog, topAmount, countryname, category,sorting)

def trendingCountry(catalog, country):
    return model.trendingCountry(catalog, country)
def trendingCategory(catalog, category):
    return model.trendingCategory(catalog, category)

def mostLiked(catalog, tag, number, country):
    return model.mostLiked(catalog, tag, number, country)
    
