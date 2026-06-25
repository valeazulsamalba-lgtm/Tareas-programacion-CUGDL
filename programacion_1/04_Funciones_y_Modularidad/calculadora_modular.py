def suma(numero1, numero2):
    resultado=numero1+numero2
    return resultado
def resta (numero1, numero2):
    resultado=numero1-numero2
    return resultado
def multiplicacion(numero1, numero2):
    resultado=numero1*numero2
    return resultado
def division(numero1, numero2):
    resultado=numero1/numero2
    return resultado


opcion = 0 
while opcion != 5:
    
    opcion = int(input("selecciona una opcion: \n 1: suma \n 2: resta \n 3: multiplicacion \n 4: division \n 5:salir \n opcion:"))

    if opcion == 1:
        print ("suma")
        num1 = float(input("ingresa numero 1:"))
        num2 = float(input("ingresa el numero 2:"))
        res=suma(num1, num2)
        print("el resultado es:", res)
    elif opcion == 2:
        print("resta")
        num1 = float(input("ingresa numero 1:"))
        num2 = float(input("ingresa numero 2:"))
        res=resta(num1, num2)
        print("el resultado es:", res)
    elif opcion == 3:
        print("multiplicacion")
        num1 = float(input("ingresa numero 1:"))
        num2 = float(input("ingresa numero 2:"))
        res=multiplicacion(num1, num2)
        print("el resultado es:", res)
    elif opcion == 4:
        print("division")
        num1 = float (input("ingresa numero 1:"))
        num2 = float (input("ingresa el numero 2:"))
        res=division(num1, num2)
        print("tu resultado es:", res)
    elif opcion == 5:
        print("saliendo.....")
    else:
        print("opcion no valida")
    input("presionar enter para continuar....")