from bs4 import BeautifulSoup as bs
import openpyxl as xl
import requests
from openpyxl import Workbook


#Toma la lista de elementos, limpia caracteres especiales y los agrega a una lista
def limpiarPalabras(listaElementos):
    print("Se han encontrado " + str(len(listaElementos)) + " palabras.")
    print("Limpiando resultados...")
    listaPalabras = []
    for x in range(len(listaElementos)):
        elemento = listaElementos[x].text
        elemento = elemento.replace('\xa0','')
        elemento = elemento.strip()
        if len(elemento)>1:
            listaPalabras.append(elemento)
    return listaPalabras

#Toma la lista de elementos y las escribe en fila en Excel.
def escribirPalabras(listaPalabras):
    print("Escribiendo palabras en Excel...")
    x=0
    for r in range(len(listaPalabras)):
        r+=1 #Tengo que empezar en 1, no puede haber fila o columna 0
        ws.cell(row=r, column=1).value = listaPalabras[x]
        x+=1

def establecerConexion(sitio):
    print("Conectando con el sitio...")
    respuesta = requests.get(sitio)
    if respuesta.status_code == 200:
        print("Se ha conectado con el sitio exitosamente.")
    elif respuesta.status_code == 404:
        print("El sitio no ha sido encontrado.")
    else:
        print("Hubo un error al ir a buscar el sitio.")
    return respuesta

respuesta = establecerConexion("https://antenario.wordpress.com/archivo-de-neologismos/")
 
soup = bs(respuesta.text,'lxml') #Proceso la respuesta de establecer conexion
lista = soup.find_all('strong') #Necesito encontrar todas las etiquetas "strong" porque ahí se alojan las palabras
palabras = limpiarPalabras(lista) #Tengo que extraer la palabra de todo el contenido de la etiqueta
wb = Workbook()  #Carga en memoria un excel
ws = wb.active  #Carga en memoria una hoja
ws.title = "Palabras a comparar" #Le agrego un nombre a la hoja
escribirPalabras(palabras) #Empiezo a cargar las palabras en la hoja
print("Guardando Excel...") #Aviso que va a guardar
wb.save("PalabrasAComparar.xlsx") #Le pido que guarde el excel con un nombre
print("Excel guardado como \"PalabrasAComparar.xlsx\" ") #Aviso el nombre con el que se guardó el archivo.

