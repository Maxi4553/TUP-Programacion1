##Ejercicio 1
# # anos_pc = int(input("Ingrese los años que tiene su computadora: "))

# # if (anos_pc <= 2):
# #     print("El computador es nuevo")
# # else:
# #     print("El computador es viejo")

##Ejercicio 2 
# num = int(input("Ingrese un número: "))

# if (num < 0):
#     print("Error")
# else:
#     print(f"El número ingresado es {num}")

##Ejercicio 3 
# nombre_1 = input("Ingrese el nombre de la primera persona: ").upper()
# nombre_2 = input("Ingrese el nombre de la segunda persona: ").upper()

# if (nombre_1 == nombre_2):
#     print(f"Los nommbre coinciden, nombre 1: {nombre_1} nombre 2: {nombre_2}")
# else:
#      print(f"Los nommbre no coinciden, nombre 1: {nombre_1} nombre 2: {nombre_2}")

##Ejercicio 4 
# print("Candidato A partido rojo, Candidato B partido verde , Candidato C partido azul")
# opcion = input("Ingrese a que candidato desea votar (A, B ,C): ").upper()

# if (opcion == "A"):
#     print("Usted a votado al candidato A PARTIDO ROJO")
# elif (opcion == "B"):
#     print("Usted a votado al candidato B PARTIDO VERDE")
# elif (opcion == "C"):
#     print("Usted a votado al candidato C PARTIDO AZUL")
# else:
#     print("Opción erronea")

##Ejercicio 5
# letra = input("Ingres una letra: ").upper()

# if(len(letra) ==  1):
#     if((letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U") ):
#         print("Es vocal")
#     else:
#         print("No es vocal")
# else:
#     print("No se puede procesar el dato")

##Ejercicio 6
# ano_bisiesto = int(input("Ingrese un año para saber si es bisiesto: "))

# if ((ano_bisiesto % 4 == 0) and (ano_bisiesto % 100 !=0)):
#     print(f"El año {ano_bisiesto} es bisiesto")
# elif (ano_bisiesto % 400 == 0):
#     print(f"El año {ano_bisiesto} es bisiesto")
# else:
#     print(f"El año {ano_bisiesto} no es bisiesto")

##Ejercicio 7
# num_1 = int(input("Ingrese un número: "))
# num_2 = int(input("Ingrese un número: "))
# num_3 = int(input("Ingrese un número: "))

# if ((num_1 < num_2) and (num_1 < num_3)):
#     print(f"El número {num_1} es el menor")
# elif ((num_2 < num_1) and (num_2 < num_3)):
#     print(f"El número {num_2} es el menor")
# else:
#     print(f"El número {num_3} es el menor")

##Ejercicio 8 
# usuario = input("Ingrese su nombre de usuario: ")

# if(usuario == "Gwenevere"):
#     contrasena = input("Ingrese su contraseña: ")
#     if(contrasena == "excalibur"):
#         print("Usuario y contraseña correctos")
#     else:
#         print("Acceso denegado")
# else:
#     print("Acceso denegado")

##Ejercicio 9

##Ejercicio 10
# edad_cliente = int(input("Ingrese la edad del cliente: "))

# if (edad_cliente < 4):
#     print("Puede entrar gratis")
# elif(edad_cliente >= 4 and edad_cliente <= 18):
#     print("Debe pagar $500")
# else:
#     print("Debe pagar $1000")

##Ejercicio 11
# ingredientes_vegetarianos = ("Pimiento","Tofu")
# ingredientes_no_vegetarianos = ("Peperoni", "jamón", "Salmón")

# pizza_deseada = input("Que tipo de pizza desea (A:vegetariana o B:no vegetariana): ").upper()

# if(pizza_deseada == "A"):
#     opcion = input("Seleccione ingredientes para pizzas vegetarianas 1(Pimiento) o 2(Tofu): ")
#     if (opcion == 1):
#         print("Su pizza vegetariana quedo compuesta por los siguientes ingredientes: tomate, mozzarella y pimiento")
#     else:
#           print("Su pizza vegetariana quedo compuesta por los siguientes ingredientes: tomate, mozzarella y tofu")
# else:
#     opcion = input("Seleccione ingredientes para pizzas no vegetarianas 1(Peperoni),  2(Jamón) o 3(Salmón): ")
#     if (opcion == 1):
#         print("Su pizza no vegetariana quedo compuesta por los siguientes ingredientes: tomate, mozzarella y peperoni")
#     elif(opcion == 1):
#         print("Su pizza no vegetariana quedo compuesta por los siguientes ingredientes: tomate, mozzarella y jamon")      
#     else:
#         print("Su pizza no vegetariana quedo compuesta por los siguientes ingredientes: tomate, mozzarella y Salmón")    
          


##Ejercicio 12

# ano_actual = int(input("Ingrese el año actual: "))
# ano_cualquiera = int(input("Ingrese un año cualquiera: "))

# if (ano_actual > ano_cualquiera):
#     diferencia = ano_actual - ano_cualquiera
#     print(f"Pasaron {diferencia} años desde {ano_actual} a {ano_cualquiera} ")
# else:
#     diferencia = ano_cualquiera - ano_actual
#     print(f"Faltan {diferencia} años para llegar de {ano_actual} a {ano_cualquiera}")

##Ejercicio 13
# num_1 = int(input("Ingrese un número positivo y mayor a cero: ")) 
# num_2 = int(input("Ingrese un número positivo y mayor a cero: ")) 


# if (num_1 > 0 and num_2 > 0):
#     if (num_1 > num_2):
#         if (num_1 % num_2 == 0):
#             print(f"El número {num_1} es múltiplo de {num_2}")
#         else:
#             print(f"El número {num_1} no es múltiplo de {num_2}")
#     else:
#         if (num_2 % num_1 == 0):
#              print(f"El número {num_2} es múltiplo de {num_1}")
#         else:
#             print(f"El número {num_2} no es múltiplo de {num_1}")
# else:
#     print("Uno de los 2 números no es mayor a 0")

##Ejercicio 14

# a = float(input("Ingrese el valor del coeficiente a: "))
# b = float(input("Ingrese el valor del coeficiente b: "))

# if (a != 0):
#     print("Solución única")
#     x= -b/a
#     print(f"La solucion para {a}x + {b}  es {x}")
# elif (a == 0 and b == 0):
#     print("Tiene infinitas soluciones")
# else:
#     print(f"La ecuación {a}x + {b} no tiene solución")

##Ejercicio 15
#consulta = input("Que area desea calcular t(triángulo) o c(círculo): ").lower()

# if (consulta == "t" or consulta == "c"):
#     if (consulta == "t"):
#         base = float(input("Ingrese la base del triángulo: "))
#         altura = float(input("Ingrese la altura del triángulo: "))
#         area = (base * altura)/2

#         print(f"El area del triángulo con base: {base} y altura: {altura} es: {area}")
#     else:
#         pi = 3.1416
#         radio = float(input("Ingrese el radio del circulo: "))
#         area = pi * radio**2
        
#         print(f"El area del circulo con radio: {radio} es: {area}")
# else:
#     print("Opción invalida, vuelva a intentarlo")

##Ejericio 16
# a = float(input("Ingrese un número a calcular: "))
# b = float(input("Ingrese un número a calcular: "))

# opcion = input("Ingrese que operacion desea realizar 1(SUMA), 2(MULTIPLICACIÓN), 3(RESTA), 4(DIVISION): ")

# if (opcion == "1"):
#     operacion = a + b
#     print(f"{a} + {b} = {operacion}")
# elif (opcion == "2"):
#     operacion = a * b
#     print(f"{a} * {b} = {operacion}")
# elif (opcion == "3"):
#     operacion = a - b
#     print(f"{a} - {b} = {operacion}")
# elif (opcion == "4"):
#     if (b != 0):
#         operacion = a / b
#         print(f"{a} / {b} = {operacion}")
#     else:
#         print("No se puede dividir entre 0")
# else:
#     print("Opción no valida")

##Ejercicio 17
# dia = input("Ingrese un día de la semana: ").lower()

# if (dia == "lunes"):
#     print("Es lunes")
# elif (dia == "viernes")
#     print("Es viernes")
# elif (dia == "sabado"):
#     print("Es sabado")
# elif (dia == "Domingo"):
#     print("Es domingo")
# else:
#     print(f"El dia ingresado no es niguno de los anteriores es: {dia}")

##Ejercicio 18 
# total_hs_trabajadas_mes = float(input("Ingrese las horas trabajadas en el mes: "))
# salario_x_hs = float(input("Ingrese el salario por hora: ")) 

# if (total_hs_trabajadas_mes > 48):
#     hs_extras = ((total_hs_trabajadas_mes - 48)* 0.1)*salario_x_hs
#     print(f"El empleado obtendra {hs_extras} por las horas extras")
#     salario_total = salario_x_hs * total_hs_trabajadas_mes + hs_extras
#     print(f"El salario total que cobrara el empleado es: {salario_total}")
# else:
#     salario_total = salario_x_hs * total_hs_trabajadas_mes 
#     print(f"El salario total que cobrara el empleado es: {salario_total}")

##Ejercicio 19
# cant_lapices = int(input("Cuantos lapices desea comprar: "))
# if (cant_lapices >= 1000):
#     descuento = round((cant_lapices * 60) * 0.07, 2)
#     precio_total = (cant_lapices * 60) - descuento
    
#     print(f"El precio a pagar por {cant_lapices} lapices es de: {precio_total}")
# else:
#     precio_total =(cant_lapices * 60)
#     print(f"El precio a pagar por {cant_lapices} lapices es de: {precio_total}")

##Ejericicio 20
# nota_1 = float(input("Ingrese la primera nota: "))
# nota_2 = float(input("Ingrese la segunda nota: "))
# nota_3 = float(input("Ingrese la tercera nota: "))
# nota_4 = float(input("Ingrese la cuarta nota: "))

# promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4 

# if (promedio >= 6):
#     print(f"Aprobado, promedio: {promedio}")
# else:
#     print(f"Desaprobado, promedio: {promedio}")






