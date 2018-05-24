print("\n")
"""Formulas a utilizar:
Indice masa corporal = peso persona/(altura)^2
depende del valor que te de indicar si es alto o bajo:
menos de 16.00 = delgadez severa infrapeso
16.00 a 16.99 = delgadez moderada
17.00 a 18.49 = delgadez aceptable
18.5 a 24.99 = normal
25.00 a 29.99 = sobrepeso
30 a 34.99 = obeso tipo 1
35 a 40 = obeso tipo 2
mas de 40 = obeso tipo 3"""

def pedirDatos():
    while True:
        try:
            peso = float(input("Ingrese su peso en kilos: "))
            altura = float(input("Ingrese su altura en metros: "))
        except:
            print("Debe ser un número")
        else:
            print (peso)
            print (altura)
            return False, peso, altura

def calculoIMC(peso, altura):
    resultado = round(peso/(altura**2),2)
    if (resultado<0):
        print("No se admiten números negativos")
    elif(resultado < 16.00):
        print("Usted tiene delgadez severa o infrapeso")
    elif (resultado >= 16.00) & (resultado <= 16.99):
         print("Usted tiene delgadez moderada")
    elif (resultado >=17.00) & (resultado <=18.49):
        print("Usted tiene delgadez aceptable")
    elif (resultado >=18.50) & (resultado <=24.99):
        print("Usted tiene un IMC normal")
    elif (resultado >=25.00) & (resultado <=29.99):
        print("Usted tiene sobrepeso")
    elif (resultado >=30.00) & (resultado <=34.99):
        print("Usted tiene obesidad tipo 1")
    elif (resultado >=35.00) & (resultado <=40.00):
        print("Usted tiene obesidad tipo 2")
    elif (resultado >40.00):
        print("Usted tiene obesidad tipo 3")
    else:
        print("No introdujo valores válidos")


pedirDatos()

