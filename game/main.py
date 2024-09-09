import random

def dato_jugador(jugador1,jugador2):
    print(f"{jugador1} y {jugador2} tienen que elegir una opcion")
    return jugador1,jugador2
    

def opciones():
    options = ('piedra', 'papel', 'tijera')
    while True:
        user_option = input('piedra, papel o tijera => ')
        user_option = user_option.lower()
        if not user_option in options:
            print('esa opcion no es valida')
        else:
            break
    computer_option = random.choice(options)
    return user_option,computer_option

def game_run():
    contadorjug1 = 0
    contadorjug2 = 0
    rounds = 1
    jugador1,jugador2 = dato_jugador(input("ingrese tu nombre: "),input("ingrese tu nombre: "))
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        rounds = rounds + 1
        eleccion1,eleccion2 = opciones()
        if eleccion1 == "piedra" and eleccion2 == "tijera" or eleccion1 == "tijera" and eleccion2 == "papel" or eleccion1 == "papel" and eleccion2 == "piedra":
            print(f"{jugador1} escogio: {eleccion1} y {jugador2} escogio: {eleccion2}")
            print(f"{jugador1} gana la ronda")
            contadorjug1 += 1
            if contadorjug1 == 3:
                print(f"{jugador1} ha ganado 3 veces y la partida")
                break
        
        elif eleccion1 == eleccion2:
            print(f"{jugador1} escogio: {eleccion1} y {jugador2} escogio: {eleccion2}")
            print("ha habido un empate")
        
        else:
            print(f"{jugador1} escogio: {eleccion1} y {jugador2} escogio: {eleccion2}")
            print(f"{jugador2} gana la ronda")
            contadorjug2 += 1
            if contadorjug2 == 3:
                print(f"{jugador2} ha ganado 3 veces y la partida")
                break

game_run()