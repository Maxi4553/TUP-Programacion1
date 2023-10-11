from funciones import *
##Ejercicio 1
# dni = input("Ingrese su número de documento: ")

# print(verificar_dni(dni))

##Ejercicio 2

# string = input("Ingrese una palabra: ")
# cont = 0
# print(long_string(string,cont))

##Ejercicio 3 

# while(True):
#     nombre = input("Ingrese su o sus nombres (Para finalizar el ingreso de socios ingrese un nombre vacio): ").title()
#     if(nombre == " "):
#         break
#     else:
#         apellido = input("Ingrese su apellido: ").title()
#         id = ""
#         dni = input("Ingrese su dni: ")
#         if(len(dni)>=7 and len(dni)<=8):
#             print("DNI ingresado correctamente")
#         else:
#             print("Su DNI debe contener entre 7 y 8 digitos")
#             dni = input("Ingrese su dni correctamente: ")

# socios_club(nombre,apellido,dni,id)

##Ejercicio 4
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# numero_multiplo(num1,num2)

##Ejercicio 5
# days = int(input("Ingrese la cantidad de dias que se introduciran: "))
# for i in range(days):
#     temp_min = float(input("Ingrese la temperatura minima del día: "))
#     temp_max = float(input("Ingrese la temperatura maxima del día: "))
#     temp_media(temp_min, temp_max)

##Ejercicio 6
# text = input("Ingrese un texto: ")

# print(cadena_espacios(text))

##Ejercicio 7 
# num = [2,3,4,5,6,7,16,12]

# print(mayor_menor_num(num))

##Ejercicio 8 
# radio = float(input("Ingrese el radio de la circunferencia: "))

# print(area_perim_circunferencia(radio))

##Ejercicio 9 
# user = input("Ingrese su usuario: ")
# contra = input("Ingrese su contraseña: ")

# print(login(user,contra))

##Ejercicio 10
phrase = input("Ingrese una frase: ")

separar_frase(phrase)