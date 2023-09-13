#Ejercicio 1--Ingles
x = 0

while x < 30:
    if x == 15:
        print(f'The execution of the loop was broken when x was {x}')
        break
    elif x==4 or x==6 or x == 10:
        print(f"The value {x} of x was skipped" )
    else:
        print(f"The value of the loop is: {x}")
    x += 1

#Ejercicio 1
while True:
    line = input("Ingrese una palabra (deje en blanco para finalizar): ").upper()
    
    if line != "":
        print(line) 
    else:
        break

#Ejercicio 2
balance = 0
while True:
    operation = input("Ingrese que operacion desea realizar D(depositar) o R(retiro). Para salir deje un espacio vacio: ").lower()

    if operation == "d":
        print("DEPOSITO")
        deposit = float(input("Ingrese cuanto dinero desea depositar: "))
        if deposit > 0:
            print("Dinero depositado correctamente")
            balance = balance + deposit
            print(f"Dinero disponible= {balance}  ")
        else:
            print("Debe ingresar un monto mayor a 0")

    elif operation == "r":
        withdrawal = float(input("Ingrese cuanto dinero desea retirar: "))
        if withdrawal > balance:
            print(f"No se pudo realizar el retiro, no cuenta con saldo suficiente, su saldo es: {balance}")
        else:
            print("Dinero depositado correctamente")
            balance = balance - withdrawal
            print(f"Dinero disponible= {balance}  ")
    elif operation == "":
        break
    else:
        print("Opcion no valida.")

print(f"Su saldo final es de: {balance}")

#Ejercicio 3
while True :
    num = int(input("Ingrese un número distinto de 0: "))
    divisores = 0 
    if num == 0:
        break
    else:
        for i in range(1,num+1):
            if num % i == 0:
                divisores +=1
            else:
                continue
    if divisores == 2:
        print(f"Es primo, {num}")  
    else:
        print(f"No es primo, {num}")  

#Ejercicio 4 
anio_1 = int(input("Ingrese un año: "))
anio_2 = int(input("Ingrese otro año: "))

for i in range(anio_1,anio_2+1):
    if (i % 4 == 0) and (i % 100 !=0) :
        if i % 10 == 0:
            print(f"El año {i} es bisiesto y multiplo de 10 ")
        else:
            print(f"El año {i} es bisiesto, pero no es multiplo de 10 ")
    elif (i % 100) and (i % 400 == 0):
        if i % 10 == 0:
            print(f"El año {i} es bisiesto y multiplo de 10 ")
        else:
            print(f"El año {i} es bisiesto, pero no es multiplo de 10 ")
    else:
        continue


#Ejercicio 5
for i in range(1,20):
    if i % 2 == 0:
        print(i)
    else:
        continue


#Ejercicio 6
num=[1,2,3,4,5,6,7,8,9,10]
search = int(input("Ingrese un número del 1 al 10 para buscarlo: "))
for i in num:
    if i == search:
        break
    else:
        continue
print(f"Se encontro el número {search}")


#Ejercicio 7
print("Elija una opción: \n _1 \n _2 \n _3 \n _4 ")
option = 1

while option != 0: 
    option = int(input("Elija una de las opciones: "))
    
    if option !=0: 
        if option == 1 or option == 2 or option == 3 or option == 4:
            print(f"La opción selccionada es: {option}")
            continue
        else:
            print("Opcion no valida")
    else:
        break