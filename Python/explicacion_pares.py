lista = ["Facundo", "Catalina", "Marina", 125, 2.3]


#Recorrer la lista con un while
#Recorrer la lista con un for
#Comparar si el segundo valor es Marina, si no lo es, imprimir el valor que sea
#Comparar si 125 > 2.3 (con variables), imprimir si lo es o no.


x=0
print ("Con While: ")
while x<len(lista):
    print(lista[x])
    x+=1

print("Con for: ")
for c in lista:
    print(c)

print("Con if:")

if lista[1]=="Marina":
    print("El valor está bien")
else:
    print(lista[1] + " es el valor correcto")

if (lista[3]>lista[4]):
    print(str(lista[3])+" es mayor a " + str(lista[4]))
else:
    print(str(lista[3]) + " es menor a " + str(lista[4]))