# Pedir datos
peso = float(input("Ingresa tu peso en kg:"))
estatura = float(input("Ingresa tu estatura en metros:"))

# Calcular IMC
imc = peso / (estatura ** 2)

print("Tu IMC es:", round(imc, 2))

# Clasificación
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc <= 24.9:
    print("Clasificación: Normal")
elif imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")