# Función para agregar pasajeros a la lista de viajeros
def agregar_pasajero():
    tupla_pasajeros = ()
    nombre = input("Ingrese el nombre del pasajero: ").title()
    dni = int(input("Ingrese el DNI del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ").title()
    tupla_pasajeros = (nombre,dni,destino)
    return(tupla_pasajeros)

def agregar_ciudad():
    tupla_pais = ()
    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el pais al cual pertenece la ciudad: ")
    tupla_pais = (ciudad,pais)
    return(tupla_pais)
    
def buscar_destino_por_dni(pasajeros):
    dni = int(input("Ingrese el DNI del pasajero: "))
    for nombre, dni_pasajero, destino in pasajeros:
        if dni_pasajero == dni:
            print(f"El pasajero {nombre} viaja a {destino}.")
            return
    print("No se encontró un pasajero con ese DNI.")

def contar_pasajeros_ciudad(pasajeros):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for _, _, destino in pasajeros if destino == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es {count}.")


def buscar_pais_dni(pasajeros, ciudades):
    dni = int(input("Ingrese el DNI del pasajero: "))
    for _, dni_pasajero, destino in pasajeros:
        if dni_pasajero == dni:
            for ciudad, pais in ciudades:
                if ciudad == destino:
                    print(f"El pasajero viaja a {ciudad}, que pertenece a {pais}.")
                    return
    print("No se encontró un pasajero con ese DNI.")

def contar_pasajeros_pais(ciudades):
    pais = input("Ingrese el nombre del país: ").title()
    count = sum(1 for _, destino in ciudades if destino == pais)
    print(f"La cantidad de pasajeros que viajan a {pais} es {count}.")
