import random
from colorama import Fore, Style, init

init(autoreset=True)

banner = r"""
  _     _            _    _            _                         _            _ _ _ 
 | |   | |          | |  (_)          | |                       | |          | | | |
 | |__ | | __ _  ___| | ___  __ _  ___| | _____ ___  _   _ _ __ | |_ ___ _ __| | | |
 | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / __/ _ \| | | | '_ \| __/ _ \ '__| | | |
 | |_) | | (_| | (__|   <| | (_| | (__|   < (_| (_) | |_| | | | | ||  __/ |  |_|_|_|
 |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\___\___/ \__,_|_| |_|\__\___|_|  (_|_|_)
                        _/ |                                                    
                       |__/                                                     
"""
print(Fore.GREEN + banner)
print("by fede jimenez v.1.18")
print("vivan las gueritas")

conteo_valores = {
    '1': 1,
    '2': 0,  
    '3': -1  
}

def crearMazo(numeroMazos):
    return ['baja'] * 20 * numeroMazos + ['neutra'] * 12 * numeroMazos + ['alta'] * 20 * numeroMazos

def pedirMazos():
    while True:
        try:
            numeroMazos = int(input("¿Cuántos mazos deseas usar (2, 4, 6, 8)? "))
            if numeroMazos in [2, 4, 6, 8]:
                return numeroMazos
            else:
                print("Por favor, elige entre 2, 4, 6 o 8 mazos.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def entrarenmedio():
    while True:
        try:
            porcentaje = float(input("¿Qué porcentaje de los mazos ya se ha jugado (0-100)? "))
            if 0 <= porcentaje <= 100:
                return porcentaje / 100  # Convertir a decimal
            else:
                print("Porcentaje fuera de rango. Ingrese un valor entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def laTrueCount(runningCount, cartasRestantes):
    if cartasRestantes == 0:
        return runningCount
    mazosRestantes = cartasRestantes / 52
    return runningCount / mazosRestantes

def viscaCatalunyaLliure(cartasSacadas, cartasTotales):
    mazosUsados = cartasSacadas / 52
    mazosRedondeaos = round(mazosUsados * 15) / 15
    return mazosRedondeaos

def deckPenetration(cartasSacadas, cartasTotales):
    return (cartasSacadas / cartasTotales) * 100

def meGustasAlejandra(mazo, cartasSacadas):
    runningCount = 0
    cartasTotales = len(mazo)

    print(Fore.MAGENTA + "Dedicado a A********)" + Style.RESET_ALL)
    print(f"\nHas seleccionado {len(mazo)//52} mazos, con un total de {cartasTotales} cartas.\n")

    while True:
        tipo_carta = input("Ingresa el tipo de carta(s) que salió (1: baja, 2: neutra, 3: alta) o 'r' para reiniciar, 'salir' para terminar: ").lower()

        if tipo_carta == 'salir':
            break
        elif tipo_carta == 'r':
            print(Fore.RED + "Reiniciando el programa...\n")
            juego_blackjack() 
            return  
            
            if carta in conteo_valores:
                runningCount += conteo_valores[carta]
                cartasSacadas += 1
                cartasRestantes = cartasTotales - cartasSacadas
                true_count = laTrueCount(runningCount, cartasRestantes)
                mazosUsados = viscaCatalunyaLliure(cartasSacadas, cartasTotales)
                deck_penetration = deckPenetration(cartasSacadas, cartasTotales)

                print("\n===== ESTADÍSTICAS DEL CONTEO =====")
                print(f"{Fore.CYAN}*** RUNNING COUNT: {Fore.YELLOW}{runningCount}{Fore.CYAN} ***")
                print(f"{Fore.CYAN}*** TRUE COUNT: {Fore.YELLOW}{true_count:.2f}{Fore.CYAN} ***")
                print("===================================")

                print(f"Mazos usados: {mazosUsados:.3f}")
                print(f"Cartas restantes: {cartasRestantes}")
                print(f"Deck Penetration: {deck_penetration:.2f}%\n")
            else:
                print("Entrada no válida. Por favor, ingresa '1', '2' o '3'.")

def juego_blackjack():
    print(Fore.GREEN + banner)  
    print(Fore.CYAN + "Bienvenido al increible, inigualable contador de cartas de Blackjack\n" + Style.RESET_ALL)

    numeroMazos = pedirMazos()

    mazo = crearMazo(numeroMazos)

    entrarMitad = input("¿Estás entrando a mitad de un juego? (s/n): ").lower()
    cartasSacadas = 0

    if entrarMitad == 's':
        porcentajeJugao = entrarenmedio()
        cartasSacadas = int(len(mazo) * porcentajeJugao)
        print(f"\nYa se han jugado {cartasSacadas} cartas.\n")

    comenzar = input("¿Estás listo para comenzar el conteo? (s/n): ").lower()
    if comenzar == 's':
        meGustasAlejandra(mazo, cartasSacadas)
    else:
        print("Saliendo del programa...")

# Ejecutar el programa
if __name__ == "__main__":
    juego_blackjack()
