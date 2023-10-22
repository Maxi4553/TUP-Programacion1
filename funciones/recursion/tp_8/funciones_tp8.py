import math
#Ejercicio 1
def cant_digitos(num):
    digitos = len(num)
    print(f"La cantidad de digitos que tiene el número {num} es {digitos}")

#Ejercicio 2
def potencia_de_otro(base,exponent):
    result = math.pow(base,exponent)

    if (result % exponent == 0):
        return True
    else:
        return False
    
##Ejercicio 3
