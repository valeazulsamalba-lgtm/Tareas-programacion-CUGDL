import random

print("🎨 Bienvenida al juego: Adivina el Color 🎨")

colores = ["azul", "rojo", "verde", "amarillo", "morado"]

seguir_jugando = True

while seguir_jugando:

    color_secreto = random.choice(colores)
    adivinaste = False

    print("\nLista de colores:")
    for i in range(len(colores)):
        print(f"{i + 1}. {colores[i]}")

    while not adivinaste:
        opcion = int(input("Elige el número del color: "))

        if 1 <= opcion <= len(colores):
            if colores[opcion - 1] == color_secreto:
                print("🎉 ¡Correcto! Adivinaste el color.")
                adivinaste = True
            else:
                print("No es ese color 😅 intenta otra vez.")
        else:
            print("Número inválido.")

    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta != "s":
        seguir_jugando = False

print("Gracias por jugar 💛")