import math
def verificar_dni(dni):
    if (len(dni) >= 7 and len(dni) <= 8 ):
        return("Su dni fue ingresados correctamente")
    else:
        return("El dni debe contener en 7 y 8 digitos")
    
def long_string(string,cont):
    for i in range(len(string)):
        if (string[i] != " "):
            cont += 1 
        else:
            continue
    return cont

def socios_club(nombre,apellido,dni,id):
    print(f"Nombre: {nombre} {apellido}")
    print(f"DNI: {dni}")
    nombre_id = nombre[:nombre.find(" ")]
    id =f"{nombre_id}{dni[:3]}"
    print(f"ID: {id}")
    return "Socio Cargado correctamente"

def numero_multiplo(num1, num2):
    if(num1 % num2 == 0):
        return("Los números ingresados son multiplos entre si")
    else:
        return("Los números ingresados no son multiplos entre si")
    
def temp_media(temp_min,temp_max):
    if(temp_min > temp_max):
        return("La temperatura minima no puede ser mayor que la máxima")
    else:
        temp_media_dia = 0
        temp_media_dia = (temp_min + temp_max)/2
        return(temp_media_dia)
        
def cadena_espacios(text):
    text_aux = "" 
    for i in range(len(text)):
        text_aux = text_aux + " "+ text[i]
    return(text_aux)

def mayor_menor_num(num):
    num_mayor = 0
    num_menor = num[5]
    for i in range(8):
        if (num[i]> num_mayor):
            num_mayor = num[i]

        if(num[i] < num_menor):
            num_menor = num[i]
        else:
            continue
    return(num_mayor,num_menor)

def area_perim_circunferencia(radio):
    area = round((math.pi * math.pow(radio,2)), 4)
    perimetro = round((2 * math.pi * radio),4)

    return(area,perimetro)

def login(user,contra):
    attempts = 0
    while(attempts <=3):
    
        if (user != "usuario1"):
            attempts += 1
            return("Vuelva a intentarlo")
        else:
            if (contra == "asdasd"):
                return ("Verdadero")
            else:
                attempts += 1
                return ("Vuelva a intentarlo, contraseña incorrecta")


def num_primo(num):
    divisores = 0
    for i in range(1,num+1):
        if (num % i == 0 ):
            divisores += 1
        else:
            continue
    if (divisores == 2) or (num == 2):
        return("El número ingresado es primo")
    else:
        return("El número ingresado no es primo")