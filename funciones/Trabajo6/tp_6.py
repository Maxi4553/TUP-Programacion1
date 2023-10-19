import funciones_tp6
# ##Ejercicio 1
# num = []
# while(True):
#     num_aux =int(input("Ingrese un número(si desea salir ingrese el 0): "))
#     if (num_aux != 0):
#         num.append(num_aux)
#     else:
#         break

# ##Ejercicio 2
# num_buscar = int(input("Ingrese un número que desee buscar y eliminar en caso de encontrarse: "))

# funciones_tp6.buscar_eliminar_num(num_buscar, num)
# print(num)

# ##Ejercicio 3
# funciones_tp6.sumar_elementos(num)

# ##Ejercicio 4
# num_aux = int(input("Ingrese nuevamente un número: "))
# num_nuevos = []

# funciones_tp6.nueva_lista(num_aux, num_nuevos,num)

# ##Ejercicio 5

# funciones_tp6.generar_listas_tuplas(num)

##Ejercicio 6 
# alumnos_primario = []
# alumnos_secundario = []
# print("Ingrese el nombre de pila de los alumnos del primario (ingrese x para finalizar): ")

# while(True):
#     nombre_alumno = input("Ingrese el nombre del alumno: ").title()
#     if (nombre_alumno != "X"):
#         alumnos_primario.append(nombre_alumno)
#     else:
#         break

# print("Ingrese el nombre de pila de los alumnos del secundario (ingrese x para finalizar): ")

# while(True):
#     nombre_alumno = input("Ingrese el nombre del alumno: ").title()
#     if (nombre_alumno != "X"):
#         alumnos_secundario.append(nombre_alumno)
#     else:
#         break

# funciones_tp6.mostrar_alumnos(alumnos_primario,alumnos_secundario)


##Informar qué nombres se repiten entre los alumnos de nivel primario y secundario
#funciones_tp6.alumnos_repetidos(alumnos_primario, alumnos_secundario)

##Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

#funciones_tp6.alumnos_no_repetidos(alumnos_primario, alumnos_secundario)

##Ejercicio 8
# rows = 10
# columns = 10 
# goals_team =[[0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0]
# ]   

##Mostrar y cargar resultados
# funciones_tp6.games(goals_team, rows, columns)
# funciones_tp6.resultado_equipos(goals_team,rows, columns)
# funciones_tp6.goal_diference(goals_team,rows,columns)

##Ejercicio 9

##Ejericio 10
# matrix = [[2,4,6,8],
#           [10,12,14,16],
#           [18,20,22,24],
#           [26,28,30,32]]

# ##DIAGONAL PRINCIPAL
# for i in range(4):
#    print("")
#    for j in range(4):
#       if (i == j ):
#          print(matrix[i][j],end="")
#       else:
#          print("_",end=" ")

# print(" ")

# ##DIAGONAL INVERSA

# for i in range(4):
#    print(" ")
#    for j in range(4):
#       if i+j == 3:
#          print(matrix[i][j],end=" ")
#       else:
#          print("_", end= " ")

##Ejercicio 11
# currency = {
#     'euro':'€', 
#     'dolar':'$', 
#     'yen':'¥',
#     'libra':'₤'
# }

# chose_currency = input("Ingrese el nombre de la divisa para saber su simbolo: ").lower()

# if chose_currency in currency:
#     valor = currency[chose_currency]
#     print(f"El simbolo del {chose_currency} es {valor}")
# else:
#     print("La divisa ingresada no se encuentra en el diccionario")

##Ejericicio 12

# name = input("Ingrese su nombre: ").title()
# age = int(input("Ingrese su edad: "))
# address = input("Ingrese su direccion: ").title()
# phone = int(input("Ingrese su número de telefono: "))

# user = {
#     'Nombre': name,
#     'Edad' : age,
#     'Direccion' : address,
#     'Telefono': phone   
# }

# print(f"{user['Nombre']} tiene {user['Edad']} años, vive en {user['Direccion']} y su número de teléfono es {user['Telefono']}")

##Ejercicio 13


