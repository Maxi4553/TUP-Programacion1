##Ejercicio Ahorcado
import random
words = ["MESSI", "MODRIC", "CRISTIANO"]

random_word = words[random.randint(0,2)]
print(random_word)
def game(word):
    print("Bienvenido al ahorcado, la tematica es futbolistas.")
    attempt = 0
    long_word = len(word)
    while(True):
        if attempt <= 6:
            lether = input("Ingrese una letra: ").upper()
        
            for i in range(0,long_word):
                if lether in word[i]:
                    print(lether, end=" ")
                else:
                    print(" _ ", end= "")
            attempt += 1 
        else:
            print(f"Se acabaron los intentos")
            break
    player = input("Ingresa el jugador que piensas que es: ").upper()

    if player == word:
        print(f"Adivinaste el jugador,{player}")
    else:
        print(f"El jugador que ingresaste no es valido el jugador era {word}")
    
    
game(random_word)