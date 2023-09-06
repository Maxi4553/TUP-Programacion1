#Ejercicio 1 
word = input("Ingrese un palabra: ")

for i in range(10):
    print(f"N°{i+1}: {word}")

#Ejercicio 2 
age = int(input("Ingrese su edad: "))

print("Años cumplidos: ")
for i in range(age):
    print(i+1)

#Ejercicio 3 
number = int(input("Ingrese un número entero positivo: "))

if (number>=0 or number != int):
    for i in range(number+1):
        if (i % 2 != 0):
            print(i,end=", ")
else:
    print("El numero no es entero positivo")

#Ejercicio 4 
number = int(input("Ingrese un número entero positivo: "))


if (number>=0 or number != int):
    for i in range(number,0,-1):
        print(i,end=", ")
else:
    print("El numero no es entero positivo")

#Ejercicio 5 
money_invest = int(input("Ingrese la cantidad de dinero que desea invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
years = int(input("Ingrese la cantidad de años que desea tener la inversión: "))
total_capital = 0
for i in range(ages):
    total_capital= money_invest + (money_invest * (annual_interest)/100)
    print(f"Año N°{i}: {total_capital}")

#Ejercicio 6
num = int(input("Ingrese un número entero:"))

for i in range(num+1):
    print(" ")
    for j in range(i):
        print("*",end="")

#Ejercicio 7

for i in range(11):
    print(f"Tabla del {i}: ")
    for j in range(10):
        mult=i * j
        print(f"{i} x {j} = {mult}")
        
#Ejercicio 8 CONSULTAR
number = int(input("Ingrese un número entero:"))

for i in range(number+1):
    print(" ")
    for j in range(i,0,-1):
        if j == 1:
            print(j, end="")
        elif (j % 2 != 0):
            print(j+2, end="")
        else:
            print(j+1,end="")       
#Ejercicio 9
boolean =True
while (boolean):
    password = input("Ingrese la contraseña: ")
    if (password == "2023"):
        print("Contraseña correcta,BIENVENIDO")
        boolean = False
    else:
        print("La contraseña no es correcta, vuelva a intentarlo.")

#Ejercicio 10
num = int(input("Ingrese un número: "))
i =1 
divisores =0

for i in range(1,num):
    if (i % num == 0):
         divisores = divisores + 1

if(divisores < 2):
    print("Es primo")
else:
    print("No es primo")

            
#Ejercicio 11
word = input("Ingrese una palabra: ").lower()

size = int(len(word))

for indice in range(len(word),0,-1):
    caracter = word[indice-1]
    print(caracter)

#Ejercicio 12
phrase = input("Introduzca una frase: ").lower()
letter = input("Introduzca una letra: ").lower()
cant_letter = 0
for i in phrase:
    if i == letter:
        cant_letter = cant_letter + 1
print(f"La cantidad de veces que aparece la letra {letter} es: {cant_letter}")

#Ejercicio 13
condition = " "

while (condition != "salir"):
    phrase = input("Ingrese un frase: ")
    print(phrase)
    condition = input("Si desea salir escriba 'salir' si no pulse cualquier tecla: ").lower()

#Ejercicio 14
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))
for i in range(num1, num2):
    if (i % 2 == 0):
        print(f"El número {i} es par")
    else:
         print(f"El número {i} es impar")

#Ejercicio 15
num = int(input("Ingrese un número entero mayor a 0: "))

if num>0:
    for i in range(num+1):
        if i>0:
            if num % i == 0:
                print(i)

#Ejercicio 16
cant_num = int(input("Cuantos números desea introducir: "))
num_negat =0

for i in range(cant_num):
    num = int(input("Ingrese un número: "))
    if num < 0:
        num_negat = num_negat + 1 

print(f"Se ingresaron {num_negat} números negativos")

#Ejercicio 17
phrase = input("Ingrese una frase: ").lower()
cont = 0
a = 0
e = 0
ii = 0
o = 0
u = 0
for i in phrase:
    if i == "a":
        if a == 0:
            a = a + 1
        else:
            print("Se repite la a")
    elif i == "e":
        if e == 0:
            e = e + 1
        else:
            print("Se repite la e")
    elif i == "i":
        if ii == 0:
            ii = ii + 1
        else:
            print("Se repite la i")
    elif i == "o":
        if o == 0:
            o = o + 1
        else:
            print("Se repite la o")
    elif i == "u":
        if u == 0:
            u = u + 1
        else:
            print("Se repite la u")     

print(f"El la frase {phrase} aparecen A: {a}, E: {e}, I: {ii}, O: {o}, U: {u}")

#Ejercicio 18
num1 = 0
num2 = 1
for i in range(10):
     print(num1)
     temp = num1
     num1 = num2
     num2 = temp + num2

#Ejercicio 19 
money_to_save = float(input("Cuanto dinero desea ahorrar: "))
acum = 0
while money_to_save > acum:
    money = float(input("Cuanto dinero ingresara: "))
    if money >=0:
        print("Dinero ingresado correctamente")
        acum = acum + money
    else:
        print("Ingreso no valido")
print(f"El monto ahorrado es de {acum} pesos")

#Ejercicio 20
condition = True
addition = 0

while condition != False:
    number = int(input("Ingrese número enteros a sumar: "))

    if number != 0:
        addition = addition + number
    else: 
        condition = False

print(f"La suma de los número ingresados es: {addition}")

#Ejercicio 21
highest  = 0
condition = True
while condition != False:
    number = int(input("Ingrese un número: "))
    if number != 0:
        if number >= highest:
            highest = number
    else:
        condition = False

print(f"El número mayor es: {highest}")

#Ejercicio 22
condition = True
even = 0
odd = 0
while condition != False:
    number = int(input("Ingrese números enteros positivos: "))
    
    if (number != -1 and number >= 0):
        if (number % 2 == 0):
            even = even + 1
        else:
            odd = odd + 1
    else:
        condition = False

print(f"Numeros pares ingresados: {even}")
print(f"Numeros impares ingresados: {odd}")

#Ejericicio 23 24
condition = True
amount = 0
while condition != False:
    purchase = float(input("Ingrese el monto de la compra: "))

    if purchase != 0:
        amount = amount + purchase
    elif (purchase < 0):
        purchase = float(input("Ingrese el monto de la compra: "))
    else:
        condition = False

if (amount > 1000):
    total = amount - (amount * 0.1)
    print(f"El monto a pagar es de: {total}")
else:
    print(f"El monto a pagar es de: {amount}")

#Ejercicio 25
number = int(input("Ingrese un número entoero para conocer su factorial: "))
factorial = 1
if number == 0 or number == 1:
    print(number)
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print(factorial)







