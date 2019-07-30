'''while True:  #Siempre pasa esto
    name = input("Ingrese usuario: ") #Pido un usuario
    if name=="Facundo": #Si el usuario es Facundo entonces va a pedir la contraseña, sino vuelve a pedir usuario
        passwd=input("Ingrese contraseña: ") #Pide contraseña
        if passwd=="123": #Si la contraseña es 123 entonces te deja pasar
            print("Bienvenido")
            break  #Si te deja pasar entonces te saca del while
        else:
            print("Contraseña incorrecta") #Si la contraseña es incorrecta
            continue  #Continue te devuelve al principio del loop
    else:
        print("Usuario incorrecto") #Si el usuario es incorrecto
        continue #Continue te devuelve al principio del loop'''

#puedo intentar hacer uno con while , if , elif y else?

while True:
    country = input("Ingrese su pais de origen: ")
    if country=="Argentina":
            print("Bienvenido/a a casa")
    elif country=="Chile":
        print("Bienvenido, ctm")
    elif country=="Uruguay":
        print("Bienvenido.El mate es argentino")
    else:
        passport= input("ingrese su número de pasaporte:")
        if passport!="123":
            print("Ese no es un pasaporte válido")
            continue
        else:
            print("Bienvenido/a a Argentina")
    break #Arregla la identacion en todo, esta desordenada, no uses espacios, usa TAB para mas facilidad
        #Estoy intentando entender el FOR.