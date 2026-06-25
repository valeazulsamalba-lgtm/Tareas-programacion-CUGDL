saldo= 1000
opcion = 0
while opcion != 4:
    opcion=int(input("elige una opcion \n 1. depositar \n 2. retirar \n 3. consultar saldo \n 4. salir \n opcion:"))
    if opcion == 1:
        #depositar
        deposito =float(input("ingresa el saldo a depositar:"))
        saldo =saldo+deposito
        print("tu nuevo saldo es:", saldo)
    elif opcion ==2:
        retirar =float(input("ingresa monto a retirar:"))
        saldo = saldo-retirar
        print("tu nuevo saldo es:", saldo)
    elif opcion==3:
        print("tu saldo es:", saldo)
    elif opcion==4:
        print("saliendo....")
