import random

player_1_points = 0
bot_points = 0

print("Bienvenido al cachi pum")
games = int(input("¡Cuantos partidas desea jugar?"))
rounds = 0
games_played = 0
option = " "
while option != "n":
    for i in range(3):
        print(f"RONDA {i+1}: ")
        player_1 = input("Jugador 1 elija una opción: \n 1:Piedra \n 2:Papel \n 3:Tijera \n ")
        player_2 = str(random.randint(1,3))
        print(player_2)
        if player_1 == "1" and player_2 == "3":
            print(f"La ronda {i+1} la gano el jugador 1")
            player_1_points +=1 
        elif player_1 == "2" and player_2 == "1":
            print(f"La ronda {i+1} la gano el jugador 1")
            player_1_points +=1 
        elif player_1 == "3" and player_2 == "2":
            print(f"La ronda {i+1} la gano el jugador 1")
            player_1_points +=1 
        elif player_1 == "1" and player_2 == "2":
            print(f"La ronda {i+1} la gano la maquina")
            bot_points +=1 
        elif player_1 == "3" and player_2 == "1":
            print(f"La ronda {i+1} la gano la maquina")
            bot_points +=1 
        elif player_1 == "2" and player_2 == "3":
            print(f"La ronda {i+1} la gano la maquina")
            bot_points +=1 
        else:
            print(f"Empate en la ronda {i+1}")
    if player_1_points > bot_points:
        print("El ganador es el jugador 1")
    elif bot_points > player_1_points:
         print("Gano la maquina")
    else:
        print("Empate, ambos ganan")

    option = input("¿Desea seguir jugando?(y/n): ").lower()
    if option == "y":
        games -= 1
        continue
    else:
        break

