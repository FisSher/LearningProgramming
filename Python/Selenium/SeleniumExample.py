from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Vamos a hacer la clasica busqueda en Google con Python.
#Porque Python es lo mejor que le paso a la automatizacion.

#Preparacion previa
driver=webdriver.Firefox() #Voy a usar el geckodriver
driver.implicitly_wait(10) #Voy a esperar 10 segundos para todas las busquedas
driver.maximize_window() #Me gusta que se maximize
#-------------------------------------
driver.get("https://www.google.com.ar/") #Vamos a google
barra_busqueda = driver.find_element_by_name("q") #Vamos a buscar la barra de busqueda
barra_busqueda.send_keys("Python org") #voy a buscar Python en google porque es el mejor lenguaje :D
barra_busqueda.send_keys(Keys.RETURN) #Voy a tocar la tecla ENTER literalmente, no la voy a escribir.
#Podria haber usado SUBMIT pero prefiero tocar el ENTER literal ya que es lo que haria el usuario promedio
resultados = driver.find_element_by_class_name("LC20lb") #Lo busco por class
resultados.click() #Le hago click

s=input("Finalizado, presione ENTER para cerrar") #Te lo dejo ver un rato hasta que le das enter para cerrar
driver.quit() #Elimino todos los procesos de firefox 