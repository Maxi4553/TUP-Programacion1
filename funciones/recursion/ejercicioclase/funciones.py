##Ejercicio 1 
import random
def jail(time):
    road = random.randint(1,3)
    if (road == 1):
        return jail(time + 3)
    elif(road == 2):
        return jail(time + 5)
    else:
        return time + 7
    
print(f"La rata tardo {jail(0)} minutos")

##Ejercicio 2 
##Escriba una función recursiva para dar vuelta un número entero

def f(n):
    s = str(n)
    if( len(s) <= 1 ):
        return s
    return s[-1] + f(int(s[:-1]))