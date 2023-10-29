import funciones_tp8
import random

#Ejercicio 1
num = input("Ingrese un número entero positivo: ")

funciones_tp8.cant_digitos(num)

#Ejercicio 2
base = int(input("Ingrese la base: "))
exponent = int(input("Ingrese el exponente: "))

print(funciones_tp8.potencia_de_otro(base, exponent))

#Ejercicio 3
phrase = input("Ingresa una frase: ")
word_in_phrase = input("Ingresa la palabra a buscar: ")
print(f"Posiciones donde se encontro {word_in_phrase} en {phrase}: {funciones_tp8.position(phrase, word_in_phrase)}")

#Ejercicio 4
number = int(input("Ingrese un numero: "))
if funciones_tp8.even(number):
    print(f"{number} es un numero par")
else:
    print(f"{number} es un numero impar")

#Ejercicio 5
array_num = []

for i in range(10):
    num = int(random.random()*100)
    array_num.append(num)

print(f"La lista es: {array_num}")
print(f"El número mas grande de la lista es: {funciones_tp8.max_list_num(array_num, 0, 0)}")

#Ejercicio 6
array_num = []
cant_num = int(input("Ingrese la cantidad de elementos que va a tener el arreglo: "))
repeat_num = int(input("Ingrese la cantidad de veces que desea que se repitan los números: "))

for i in range(cant_num):
    num = int(random.random()*5)
    array_num.append(num)

print(f"El array original: {array_num}")
print(f"El array números repetidos: {funciones_tp8.repeat_num(array_num, repeat_num)}")

#Ejercicio 7
number_1 = int(input("Ingrese el primer número: "))
number_2 = int(input("Ingrese el segundo número: "))
print(funciones_tp8.sum_recursiva(number_1,number_2))

#Ejercicio 8
print("El valor es: ", funciones_tp8.calculate_pascal(7,3))

##Ejercicio 9
characters = ["&","?","#","%","!"]
number = 3
funciones_tp8.combinations(characters,number)

#Ejercicio 10
number=1
while True:
    number=int(input("Ingrese un numero mayor que 0: "))
    if number>0:
        break
    
width, length = funciones_tp8.sheet_measurement(number)
print(f'Ancho de A{number}: {width} mm, Largo de A{number}: {length} mm')



