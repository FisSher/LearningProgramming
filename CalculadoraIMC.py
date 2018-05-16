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

def calculoIMC():
    while True:
        try:
            peso = float(input("Ingrese peso(en kilos): "))
            altura = float (input("Ingrese altura (en metros): "))
            if (peso<=0) | (altura <= 0):
                raise ValueError ('No ha utilizado un número válido para el cálculo')
            break
        except ZeroDivisionError:
            print ("Número inválido, división por cero.")
        except ValueError:
            print ("No ha utilizado un número válido para el cálculo")
        except TypeError:
            print("Valor inválido")




    resultado = round(peso/(altura**2),2)
    print ('\nSu índice de masa corporal es: ' + str(resultado))
    if (resultado<16.00):
        print("Usted posee delgadez severa o infrapeso")
    elif(resultado >= 16.00) & (resultado <= 16.99):
        print("Usted posee delgadez moderada")
    elif(resultado >= 17.00) & (resultado <= 18.49):
        print("Usted posee delgadez aceptable")
    elif(resultado >= 18.50) & (resultado <= 24.99):
        print("Usted posee un IMC normal")
    elif(resultado >= 25.00) & (resultado <= 29.99):
        print("Usted posee sobrepeso")
    elif(resultado >= 30.00) & (resultado <= 49.99):
        print("Usted posee obesidad tipo 1")
    elif(resultado >= 35.00) & (resultado <= 40.00):
        print("Usted posee obesidad tipo 2")
    elif(resultado >= 40.00):
        print("Usted posee obesidad tipo 3")
    else:
        print("Se produjo un error de datos")
    print("\nGracias por utilizar la calculadora de IMC")

def redo():
    ans = None
    ans = str.upper(input("¿Volver a calcular?(S para SI/ N para NO: "))
    if (ans == 'S'):
        calculoIMC()
    elif(ans=='N'):
        print("Hasta luego!")
    else:
        print("No es una opción válida")


calculoIMC()
redo()