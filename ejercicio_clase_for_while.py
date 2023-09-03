##Ejercicio 1
resultado = " "
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
corrimiento = int(input("Ingrese la cantidad de lugares a correr las letras: "))
for i in range(5):
    texto =input("Ingrese el mensaje a encriptar: ")
    resultado = " "
    for letra in texto:
        if letra.isalpha():
            indice = alfabeto.index(letra.upper())
            nuevo_indice = (indice + corrimiento) % 27
            nueva_letra = alfabeto[nuevo_indice]
            if letra.islower():
                nueva_letra = nueva_letra.lower()
            resultado += nueva_letra
        else:
            resultado += letra
    print(f"El mensaje {texto} encriptado es: {resultado} ")

##Ejercicio 2
pares_totales = 0
impares_totales = 0

#Se solicitaran números enteros al usuario hasta que el usaurio ingrese cero
while True:
    numero = int(input("Ingrese un número entero positivo (0 para salir): "))
    if numero == 0:
         break
    
    pares = 0
    impares = 0
    
    while numero > 0:
        digito = numero % 105
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
            numero //= 10

    
    print(f"Dígitos pares: {pares}, Dígitos impares: {impares}")
    
    pares_totales += pares
    impares_totales += impares

print(f"Total de dígitos pares ingresados: {pares_totales}")
print(f"Total de dígitos impares ingresados: {impares_totales}")