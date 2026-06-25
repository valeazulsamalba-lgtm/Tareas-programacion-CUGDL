import random
#crear una lista
cantidad_jugadores = int(input("cuantos jugadores seran:?"))
jugadores = []
contador = 0
while(contador < cantidad_jugadores):
    jugador = input("nombre del jugador:")
    jugadores.append(jugador)
    contador=contador+1
mejor_puntuaje=0
ganador=""
for jugador in jugadores:
    dado=random.randint(1,6)
    while dado ==6:
        print("el jugador", jugador, "obtuvo 6")
        dado += random.randint(1,6)
    print("el jugador", jugador, "obtuvo", dado)
    if dado>mejor_puntuaje:
        mejor_puntuaje = dado
        ganador = jugador
print("el ganador es", ganador, "con", mejor_puntuaje, "puntos")
