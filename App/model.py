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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
from DISClib.ADT import list as lt # pylint: disable=import-error
from DISClib.Algorithms.Sorting import shellsort as sa # pylint: disable=import-error
from DISClib.Algorithms.Sorting import insertionsort as ins # pylint: disable=import-error
from DISClib.Algorithms.Sorting import selectionsort as sel # pylint: disable=import-error
from DISClib.Algorithms.Sorting import mergesort as mer # pylint: disable=import-error
from DISClib.Algorithms.Sorting import quicksort as qck # pylint: disable=import-error
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(dtEstructure):
    catalog = {'videos': None,
               'categoriesId': None,"categories": None, "tags":{}} 
    catalog['videos'] = lt.newList(dtEstructure)
    catalog["categoriesId"] = lt.newList(dtEstructure) 
    catalog["categories"] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareCategories)
    
          
    return catalog
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video, dtEstructure):
    if not video["country"] in  catalog.keys():
        tc= video["country"]
        catalog[tc]= None
        catalog[tc]= lt.newList(dtEstructure)
        lt.addLast(catalog[tc], video)
    else:
        tc= video["country"]
        lt.addLast(catalog[tc], video)

    lt.addLast(catalog['videos'], video)
    addVideoCategory(catalog, video)
    tags = video["tags"].split("|")
    
    for tag in tags:
        a=tag.strip('\"')
        if not a in catalog["tags"].keys():
            catalog["tags"][a]= None
            catalog["tags"][a]= lt.newList(dtEstructure)
            lt.addLast(catalog["tags"][a], video)
        else:
             lt.addLast(catalog["tags"][a], video)

def addCategory(catalog, category):
    lt.addLast(catalog["categoriesId"], category)
def addVideoCategory(catalog, video):
    try:
        categories = catalog["categories"]
        idcategory= video["category_id"]
        existcategory= mp.contains(categories, idcategory)
        if existcategory:
            entry= mp.get(categories, idcategory)
            category= me.getValue(entry)
        else:
            category= newCategory(idcategory)
            mp.put(categories, idcategory, category)
        lt.addLast(category["videos"], video)
    except Exception:
        return None

def newCategory(idcategory):
    entry = {'category': "", "videos": None}
    entry['category'] = idcategory
    entry['videos'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry
# Funciones para creacion de datos

# Funciones de consulta
def topVideos(catalog, topAmount, countryname, category,sorting):
    for i in lt.iterator(catalog["categoriesId"]):
        if i["name"] == category:
            idnumber= i["id"]
    top= lt.newList()
    for i in lt.iterator(catalog[countryname]):
        if i["category_id"] == idnumber:
            lt.addLast(top, i)

    sortVideos(top, sorting)
    if topAmount > lt.size(top):
        print("No se puede mostrar el top "+str(topAmount)+", ya que solo existen "+str(lt.size(top))+" videos que cumplen con los filtros seleccioados")
        print("Se mostrara en cambio el top "+str(lt.size(top)))
        topAmount= lt.size(top)
    sub= lt.subList(top, 1,topAmount)
    for i in range(1, lt.size(sub)+1):
        a=lt.getElement(sub, i)
        print("Posicion: "+str(i)+"|"+"Titulo: "+a["title"]+"|Canal: "+a["channel_title"]+"|Fecha publicacion: "+a["publish_time"]+"|Vistas: "+a["views"]+"|Likes: "+a["likes"]+"|Dislikes: "+a["dislikes"])

def trendingCountry(catalog, country):
    lista= {}
    for i in lt.iterator(catalog[country]):
        if not i["title"] in lista.keys():
            lista[i["title"]]= None
            lista[i["title"]]= 1
        else:
            lista[i["title"]]+= 1
    vid= max(lista, key= lista.get)
    for i in lt.iterator(catalog[country]):
        if i["title"] == vid:
            channel= i["channel_title"]
    print("Titulo: "+vid+"\nNombre del canal: "+channel+"\nPais: "+country+"\nNumero de dias: "+str(lista[vid]))

def trendingCategory(catalog, category):
    trending= {}
    for i in lt.iterator(catalog["categoriesId"]):
        if i["name"] == category:
            idnumber= i["id"]
    for i in lt.iterator(catalog["videos"]):
        if i["category_id"]== idnumber:
            if not i["title"] in trending.keys():
                trending[i["title"]]= None
                trending[i["title"]]= 1
            else:
                trending[i["title"]]+= 1
    vid= max(trending, key= trending.get)
    for i in lt.iterator(catalog["videos"]):
        if i["title"] == vid:
            channel= i["channel_title"]
    print("Titulo: "+vid+"\nNombre del canal: "+channel+"\nId categoria: "+idnumber+"\nNumero de dias: "+str(trending[vid]))

def mostLiked(catalog, tagname, number, country):
    lista= lt.newList()
    videos= []
    lista2= lt.newList()
    for i in lt.iterator(catalog["tags"][tagname]):
        if i["country"] == country:
            lt.addLast(lista, i)
    mer.sort(lista, cmpVideosByLikes)
    for i in lt.iterator(lista):
        if not i["video_id"] in videos:
            videos.append(i["video_id"])
            lt.addLast(lista2, i)
    sub= lt.subList(lista2, 1, number)
    for i in range(1, lt.size(sub)+1):
        a= lt.getElement(sub, i)
        print("Posicion: "+str(i)+"\nTitulo: "+a["title"]+"\nCanal: "+a["channel_title"]+"\nFecha publicacion: "+a["publish_time"]+"\nVistas: "+a["views"]+"\nLikes: "+a["likes"]+"\nDislikes: "+a["dislikes"]+"\nTags: "+a["tags"]+"\n")

def mostLikedCategories(catalog, number, category):
    for i in lt.iterator(catalog["categoriesId"]):
        if i["name"] == category:
            idnumber= i["id"]
    a=mp.get(catalog["categories"],idnumber)
    video= me.getValue(a)["videos"]
    mer.sort(video, cmpVideosByLikes)
    sub= lt.subList(video, 1, number)
    for i in range(1, lt.size(sub)+1):
        a= lt.getElement(sub, i)
        print("Nombre: "+ a["title"]+"|Categoria: "+category+"|Likes: "+a["likes"])


    


# Funciones utilizadas para comparar elementos dentro de una lista
def comparetags(tagname1, tag):
    if (tagname1.lower() in tag['name'].lower()):
        return 0
    return -1

def cmpVideosByViews(video1, video2):
    return int(video1['views']) > int(video2['views'])

def cmpVideosByLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))
def compareCategories(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0
def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0

# Funciones de ordenamiento
def sortVideos(lt, sorting):  
    if sorting == 0:
        sa.sort(lt, cmpVideosByViews)
    elif sorting == 1:
        ins.sort(lt, cmpVideosByViews)
    elif sorting == 2:
        sel.sort(lt, cmpVideosByViews)
    elif sorting == 3:
        mer.sort(lt, cmpVideosByViews)
    else:
        qck.sort(lt, cmpVideosByViews)