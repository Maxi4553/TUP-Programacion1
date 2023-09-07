#Ejercicio 1
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

perimetro = 2 * (base + altura)
area = base * altura

print(f"El area del triángulo es: {area} y su perimetro es: {perimetro}")

#Ejercicio 2
cateto_1 = float(input("Ingrese el primer cateto: "))
cateto_2 = float(input("Ingrese el segundo cateto: "))
hipotenusa = (cateto_1**2 + cateto_2**2)**(1/2)

print(f"La medida de la hipotenusa es: {hipotenusa}")

#Ejercicio 3 
num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2

print(f"SUMA: {suma}, RESTA: {resta}, DIVISION: {division}, MULTIPLICACION: {multiplicacion}")

#Ejercicio 4 
fahrenheit = float(input("Ingrese los grados fahrenheit: "))
celsius = (fahrenheit -32)* 5/9

print(f"{fahrenheit}° equivalen a {celsius}° celsius")

#Ejercicio 5
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
# El nombre de la varible esta en mayusculas(lo cual es una mala practica)
# y en el imput

#solución:
nombre = "David"
a = input(f"{nombre} ¿Cual es tu canción favorita? ")

print(f"La cancion favorita de {nombre} es: {a} ")

#b)	
#   precio = input(“Precio: “)
#   total = precio + (precio * 0.1)
# No permitira realizar las operaciones ya que el precio va ser un string

#solución:
precio = float(input("Precio: "))
total = precio + (precio * 0.1)

print(f"El precio es: {precio} ")

#c)
#   edad = int(input(“Edad: “))
#   print(tu edad es, edad)
# En el print el mensaje no se encuentra entre ""

#solición: 
edad = int(input("Edad: "))
print("tu edad es ", edad)

#d)	
#   edad = int(input("Edad: "))
#   print("Veamos si tu edad es 18…", edad=18)

# Hay una asignacion dentro del print

edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad)

#Ejercicio 6
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))
num3 = float(input("Ingrese un número: "))

media = (num1 + num2 + num3)/3

print(f"La media entre {num1}, {num2} y {num3} es: {media}")

#Ejercicio 7
minutos = int(input("Ingrese los minutos: "))
horas = minutos//60
minutos_2 = minutos - (horas * 60)

print(f"{minutos}min equivalen a {horas}hs {minutos_2}min")

#Ejercicio 8
sueldo_base = int(input("Ingrese el sueldo base del empleado: "))
comision = sueldo_base * 0.3
sueldo_mes = sueldo_base + comision

print(f"SUELDO BASE: {sueldo_base} , COMISION: {comision}, SUELDO TOTAL: {sueldo_mes}")

#Ejercicio 9
precio_neto = int(input("Ingrese el precio del producto: "))
descuento = precio_neto * 0.15
precio_total = precio_neto - descuento

print(f"PRECIO NETO: {precio_neto}, DESCUENTO: {descuento}, PRECIO TOTAL: {precio_total}")

#Ejercicio 10 
parcial1 = int(input("Ingrese la calificación del primer parcial: ")) 
parcial2 = int(input("Ingrese la calificación del segundo parcial: "))
parcial3 = int(input("Ingrese la calificación del tercerr parcial: ")) 

examen_final = int(input("Ingrese la calificación del examen final: ")) 

trabajo_final = int(input("Ingrese la calificación del trabajo final: ")) 

promedio_parcial = (parcial1 + parcial2 + parcial3) / 3 

# ​calificacion_final = (promedio_parcial * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15) 

# ​print("Su Calificacion total es: "+str(calificacion_final))

#Ejercicio 11
num1 =  int(input("Ingrese un número: "))
num2 =  int(input("Ingrese un número: "))

distancia = num1 - num2
valor_absoluto = distancia if distancia>0 else distancia*(-1)

print(f"La distancia entre {num1} y {num2} es de {valor_absoluto} ")

#Ejercicio 12 
num = int(input("Ingrese un número para saber su raiz cubica y cuadrada: "))
raiz_cuadrada = num ** (1/2)
raiz_cubica = num ** (1/3)

print(f"La raiz cuadrada de {num} es {raiz_cuadrada} y la cubica es {raiz_cubica} ")

#Ejercicio 13
num = int(input("Ingrese un número de 2 cifras: "))

aux = str(num // 10) 
aux_2 = str(num % 10) 

num_invertido = aux_2 + aux

print(f"El número {num} invertido es: {num_invertido}")

#Ejercicio 14
var_a = input("Ingrese un valor para la variable a: ")
var_b = input("Ingrese un valor para la variable b: ")

print(f"Valores originales= A= {var_a} B= {var_b}")
aux = var_a
var_a = var_b
var_b = aux
print(f"Valores intercambiados= A= {var_a} B= {var_b}")

#Ejercicio 15

#Ejercicio 16
nombre = input("Ingrese su nombre: ")
apellido_1 = input("Ingrese su primer apellido: ")
apellido_2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[0] + apellido_1[0] + apellido_2[0] 

print(f"Nombre completo {nombre} {apellido_1} {apellido_2}, sus iniciales son: {iniciales}")

#Ejercicio 17
usuario = input("Ingrese su nombre: ")

print(f"Ahora su nombre esta en la matrix, {usuario}")

#Ejercicio 18
costo_cena = float(input("Ingrese el valor de su cena: "))

servicio = costo_cena * 0.062
propina = costo_cena * 0.10 

costo_total =  costo_cena + servicio + propina

print(f"Costo de la cena: {costo_cena} servicio: {servicio} propina: {propina}  COSTO TOTAL: {costo_total}")

#Ejercicio 19
dia_nacim = input("Ingrese el día de su cumpleaños: ")
mes_nacim = input("Ingrese el mes en el que cumple años: ")
ano_nacim = input("Ingrese el año el que nacio: ")

print(f"Su cumpleaños es el: {dia_nacim}/{mes_nacim}/{ano_nacim}")

#Ejercicio 20
fecha_nacim = input("Ingrese su fecha de nacimiento (DDMMAAAA): ")
dia = fecha_nacim[0:2]
mes = fecha_nacim[2:5]
anio = fecha_nacim[5:]
print(f"Su fecha de nacimiento es: {dia}/{mes}/{anio} ")

#Ejercicio 21
km_x_litro = int(input("Ingrese cuantos kilometros puede realizar por litro de combustible: "))
capacitad_tanque = int(input("Cual es la capacidad en litros del tanque: "))
km_a_recorrer = int(input("Cuantos kilometros recorreran: "))

cant_tanques_llenar = (km_a_recorrer / km_x_litro)/capacitad_tanque

print(f"La cantidad de tanques que necesita para realizar el viaje son:  {cant_tanques_llenar}")

