# MODULO 2: ESTADISTICA DESCRIPTIVA

def estadisticas(datos):

    # MEDIA
    suma = 0
    for num in datos:
        suma += num
    media = suma / len(datos)

    # MEDIANA
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)

    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    # MODA
    frecuencia = {}
    for num in datos:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())

    moda = []
    for num, frec in frecuencia.items():
        if frec == max_frecuencia:
            moda.append(num)

    # MAXIMO Y MINIMO
    maximo = max(datos)
    minimo = min(datos)

    # MOSTRAR RESULTADOS
    print("\n===== ESTADISTICAS =====")
    print("Media:", media)
    print("Mediana:", mediana)
    print("Moda:", moda)
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)

    # Regresar media para usarla en anomalías
    return media



# MODULO 4: DETECCION DE ANOMALIAS


def detectar_anomalias(datos, media):

    print("\n===== ANOMALIAS =====")

    anomalías = []

    for num in datos:

        # Ejemplo: si el valor duplica la media
        if num > media * 2:
            anomalías.append(num)

    if len(anomalías) == 0:
        print("No se detectaron anomalías.")
    else:
        print("Valores atípicos encontrados:")
        for a in anomalías:
            print(a)

    