def renderizar(matriz):
    for fila in matriz:
        print(" ".join(fila))

mapa = [
    ["🟩", "🟩", "🟩", "🟩", "🟩"],
    ["🟩", "🟩", "🟩", "🟩", "🟩"],
    ["🟩", "🟩", "🟩", "🟩", "🟩"],
    ["🟩", "🟩", "🟩", "🟩", "🟩"],
    ["🟩", "🟩", "🟩", "🟩", "🟩"],
]
renderizar(mapa)
opcion =  0
while opcion !=3:
    
    opcion=int(input("que icono quieres agregar:  \n 1: 🏡  \n 2: 🟩  \n 3:🌲 \n opcion:  "))
    
    if(opcion==1):
        emoji="🏡"
        fila=int(input("que fila:"))
        columna=int(input("que columna:"))
        mapa[fila][columna]=emoji
        renderizar (mapa)
    elif(opcion==2):
        emoji="🟩"
        fila=int(input("que fila:"))
        columna=int(input("que columna:"))
        mapa[fila][columna]=emoji
        renderizar (mapa)
    elif(opcion==3):
        emoji="🌲"
        fila=int(input("que fila:"))
        columna=int(input("que columna:"))
        mapa[fila][columna]=emoji
        renderizar (mapa)

    
fila=int(input("que fila:"))
columna=int(input("que columna:"))
mapa[fila][columna]=emoji

renderizar (mapa)
