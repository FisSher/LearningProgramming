'''while True:  #Siempre pasa esto
    name = input("Ingrese usuario: ") #Pido un usuario
    if name=="Fish": 
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


while True:
    country = input("Ingrese su pais de origen: ")
    if country=="Argentina":
            print("Bienvenido/a a casa")
    elif country=="Chile":
        print("Bienvenido a Chile")
    elif country=="Uruguay":
        print("Bienvenido a Uruguay")
    else:
        passport= input("ingrese su número de pasaporte:")
        if passport!="123":
            print("Ese no es un pasaporte válido")
            continue
        else:
            print("Bienvenido/a a Argentina")
    break 
