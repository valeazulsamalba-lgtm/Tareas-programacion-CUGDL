import random

print("🎮 Bienvenida al juego: Adivina el Número 🎮")

seguir_jugando = True

while seguir_jugando:

    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinaste = False

    while not adivinaste:
        intento = int(input("Adivina un número entre 1 y 100: "))
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo 👀 intenta un número más grande.")
        elif intento > numero_secreto:
            print("Muy alto 👀 intenta un número más pequeño.")
        else:
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
            adivinaste = True

    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()

    if respuesta != "s":
        seguir_jugando = False

print("Gracias por jugar 💛")