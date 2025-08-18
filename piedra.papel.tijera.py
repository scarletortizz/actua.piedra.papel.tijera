import random

opciones = ["piedra", "papel", "tijera"]
def limpiar():
    print(" " * 50)

def resultado(j1, j2):
    if j1 == j2:
        return "Empate"
    if (j1 == "piedra" and j2 == "tijera") or \
       (j1 == "tijera" and j2 == "papel") or \
       (j1 == "papel" and j2 == "piedra"):
        return "Jugador 1"
    return "Jugador 2"

def reglas():
    limpiar()
    print("--- Reglas ---")
    print("Piedra rompe tijera")
    print("Tijera corta papel")
    print("Papel cubre piedra\n")

def registrar(n1, n2, res, estadisticas, historial):
    for n in [n1, n2]:
        if n not in estadisticas:
            estadisticas[n] = {"ganadas": 0, "perdidas": 0, "empates": 0}

    if res == "Empate":
        estadisticas[n1]["empates"] += 1
        estadisticas[n2]["empates"] += 1
    elif res == "Jugador 1":
        estadisticas[n1]["ganadas"] += 1
        estadisticas[n2]["perdidas"] += 1
    else:
        estadisticas[n2]["ganadas"] += 1
        estadisticas[n1]["perdidas"] += 1

    historial.append({"jugador1": n1, "jugador2": n2, "resultado": res})

def mostrar_stats(estadisticas, historial, total_partidas):
    limpiar()
    if total_partidas == 0:
        print("No hay estadísticas aún.\n")
        return
    print("--- Estadísticas ---Partidas jugadas: {total_partidas}")
    for h in historial:
        print("{['jugador1'] vs ['jugador2'] → ['resultado']}")
    print("Resumen por jugador:")
    for j, d in estadisticas.items():
        print("{j}: {d['ganadas']} ganadas, {d['perdidas']} perdidas, {d['empates']} empates")
    print("")

def jugar_ronda(n1, n2, contra_pc, estadisticas, historial):
    jug1 = input("{n1}, elige piedra, papel o tijera: ").lower()
    while jug1 not in opciones:
        jug1 = input("Opción inválida. Intenta de nuevo: ").lower()

    if contra_pc:
        jug2 = random.choice(opciones)
        print("{n2} eligió: {jug2}")
    else:
        limpiar()
        jug2 = input(f"{n2}, elige piedra, papel o tijera: ").lower()
        while jug2 not in opciones:
            jug2 = input("Opción inválida. Intenta de nuevo: ").lower()

    res = resultado(jug1, jug2)
    if res == "Empate":
        print("¡Empate!")
    elif res == "Jugador 1":
        print(f"¡Ganó {n1}!")
    else:
        print(f"¡Ganó {n2}!")
    registrar(n1, n2, res, estadisticas, historial)

def menu_juego(estadisticas, historial, total_partidas):
    limpiar()
    print("--- Modos ---")
    print("1. Contra computadora")
    print("2. Multijugador")
    print("3. Volver")
    op = input("Elige: ")

    if op == "1":
        n1 = input("Nombre del jugador: ")
        n2 = "Computadora"
        while True:
            jugar_ronda(n1, n2, True, estadisticas, historial)
            total_partidas += 1
            if input("¿Otra partida? (s/n): ").lower() != "s":
                break
    elif op == "2":
        n1 = input("Nombre Jugador 1: ")
        n2 = input("Nombre Jugador 2: ")
        while True:
            jugar_ronda(n1, n2, False, estadisticas, historial)
            total_partidas += 1
            if input("¿Otra partida? (s/n): ").lower() != "s":
                break
    return total_partidas


estadisticas = {}
historial = []
total_partidas = 0

while True:
    limpiar()
    print("=== Menú Principal ===")
    print("1. Jugar")
    print("2. Reglas")
    print("3. Estadísticas")
    print("4. Salir")
    op = input("Elige: ")

    if op == "1":
        total_partidas = menu_juego(estadisticas, historial, total_partidas)
    elif op == "2":
        reglas()
        input("Presiona Enter para volver...")
    elif op == "3":
        mostrar_stats(estadisticas, historial, total_partidas)
        input("Presiona Enter para volver...")
    elif op == "4":
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción inválida.")
        input("Presiona Enter para volver...")


