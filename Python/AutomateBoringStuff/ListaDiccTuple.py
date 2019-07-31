#Demostración de como funcionan los elementos de los diferentes tipo de dato
#Se incluyen operaciones

lista = [1.0,2,3,'c'] #Coleccion variada
tupl = (10,20,30) #Ordenados, imposible modificarlos
dicc = {'nombre':'Solaire','edad' : 32, 'lista':['elem1','elem2','elem3']}
print(lista[1]+lista[2])
print(tupl[2])
for valor in dicc:
    print(valor,':',dicc[valor])