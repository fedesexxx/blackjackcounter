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
print("by fede jimenez v.1.16")
print("vivan las gueritas")

conteo_valores = {
    '1': 1,  # Cartas bajas (2, 3, 4, 5, 6)
    '2': 0,  # Cartas neutras (7, 8, 9)
    '3': -1  # Cartas altas (10, J, Q, K, A)
}

def crear_mazo(numero_de_mazos):
    return ['baja'] * 20 * numero_de_mazos + ['neutra'] * 12 * numero_de_mazos + ['alta'] * 20 * numero_de_mazos

def pedir_numero_de_mazos():
    while True:
        try:
            numero_de_mazos = int(input("¿Cuántos mazos deseas usar (2, 4, 6, 8)? "))
            if numero_de_mazos in [2, 4, 6, 8]:
                return numero_de_mazos
            else:
                print("Por favor, elige entre 2, 4, 6 o 8 mazos.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def pedir_porcentaje_mazos_jugados():
    while True:
        try:
            porcentaje = float(input("¿Qué porcentaje de los mazos ya se ha jugado (0-100)? "))
            if 0 <= porcentaje <= 100:
                return porcentaje / 100  
            else:
                print("Porcentaje fuera de rango. Ingrese un valor entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def calcular_true_count(running_count, cartas_restantes):
    if cartas_restantes == 0:
        return running_count
    mazos_restantes = cartas_restantes / 52
    return running_count / mazos_restantes

def calcular_mazos_usados(cartas_sacadas, cartas_totales):
    mazos_usados = cartas_sacadas / 52
    mazos_usados_redondeados = round(mazos_usados * 15) / 15
    return mazos_usados_redondeados

def calcular_deck_penetration(cartas_sacadas, cartas_totales):
    return (cartas_sacadas / cartas_totales) * 100

def contar_cartas_manual(mazo, cartas_sacadas):
    running_count = 0
    cartas_totales = len(mazo)
    
    print(f"\nHas seleccionado {len(mazo)//52} mazos, con un total de {cartas_totales} cartas.\n")
    print("nota: ahora puedes agregar varias cartas a la vez en el mismo imput (ej: 223 [dos neutras y una alta])")
    while True:
        tipo_carta = input("Ingresa el tipo de carta que salió (1: baja, 2: neutra, 3: alta) o 'r' para reiniciar, 'salir' para terminar: ").lower()
        
        if tipo_carta == 'salir':
            break
        
        if tipo_carta == 'r':
            print("\nReiniciando el programa...\n")
            juego_blackjack()  
            return
        
        for carta in tipo_carta:
            if carta in conteo_valores:
                running_count += conteo_valores[carta]
                cartas_sacadas += 1
                cartas_restantes = cartas_totales - cartas_sacadas
                true_count = calcular_true_count(running_count, cartas_restantes)
                mazos_usados = calcular_mazos_usados(cartas_sacadas, cartas_totales)
                deck_penetration = calcular_deck_penetration(cartas_sacadas, cartas_totales)
                
                print("\n===== ESTADÍSTICAS DEL CONTEO =====")
                print(f"{Fore.CYAN}*** RUNNING COUNT: {Fore.YELLOW}{running_count}{Fore.CYAN} ***")
                print(f"{Fore.CYAN}*** TRUE COUNT: {Fore.YELLOW}{true_count:.2f}{Fore.CYAN} ***")
                print("===================================")
                
                print(f"Mazos usados: {mazos_usados:.3f}")
                print(f"Cartas restantes: {cartas_restantes}")
                print(f"Deck Penetration: {deck_penetration:.2f}%\n")
            else:
                print(f"Entrada no válida para la carta: {carta}. Por favor, ingresa '1', '2' o '3'.")

def juego_blackjack():
    while True:
        print(Fore.GREEN + banner)
        print(Fore.CYAN + "Bienvenido al contador de cartas de Blackjack\n" + Style.RESET_ALL)

        numero_de_mazos = pedir_numero_de_mazos()
        
        mazo = crear_mazo(numero_de_mazos)

        entrar_mitad = input("¿Estás entrando a mitad de un juego? (s/n): ").lower()
        cartas_sacadas = 0

        if entrar_mitad == 's':
            porcentaje_jugado = pedir_porcentaje_mazos_jugados()
            cartas_sacadas = int(len(mazo) * porcentaje_jugado)
            print(f"\nYa se han jugado {cartas_sacadas} cartas.\n")

        comenzar = input("¿Estás listo para comenzar el conteo? (s/n): ").lower()
        if comenzar == 's':
            contar_cartas_manual(mazo, cartas_sacadas)
        else:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    juego_blackjack()
