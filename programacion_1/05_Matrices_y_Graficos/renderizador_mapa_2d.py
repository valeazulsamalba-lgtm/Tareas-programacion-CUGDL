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

mapa[1][1]="🌲"
mapa[2][1]="🌲" 
mapa[3][1]="🌲"
mapa[1][2]="🌲"
mapa[1][3]="🌲"
mapa[3][2]="🌲"
mapa[2][3]="🌲"
mapa[3][3]="🌲"
mapa[2][2]="🏡"
renderizar (mapa)