#Ejercicio 1 
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

#Ejercicio 2
def obtener_domicilios_factura(compras):
    domicilios_factura = set()
    
    for compra in compras:
        cliente, _, _, domicilio = compra  # Ignoramos el día y el monto
        domicilios_factura.add(domicilio)
    
    return list(domicilios_factura)

#Ejercicio 3 
socios = {
    1: {'nombre': 'Amanda Núñez', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    2: {'nombre': 'Bárbara Molina', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True}
}
def informar_cantidad_socios():
    print(f"El club tiene {len(socios)} socios.")

def pagar_cuotas(socio_numero):
    if socio_numero in socios:
        socios[socio_numero]['cuota_al_dia'] = True
        print(f"El socio n°{socio_numero} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"El socio n°{socio_numero} no se encuentra en la lista de socios.")

# Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018
def modificar_fecha_ingreso():
    for socio_numero, datos_socio in socios.items():
        if datos_socio['fecha_ingreso'] == '13/03/2018':
            datos_socio['fecha_ingreso'] = '14/03/2018'

# Solicitar el nombre y apellido de un socio y darle de baja
def dar_de_baja(nombre_apellido):
    for socio_numero, datos_socio in socios.copy().items():
        if f"{datos_socio['nombre']} {datos_socio['apellido']}" == nombre_apellido:
            del socios[socio_numero]
            print(f"El socio {nombre_apellido} ha sido dado de baja.")

# Función para imprimir el listado de socios completo
def imprimir_listado_socios():
    print("Listado de Socios:")
    for socio_numero, datos_socio in socios.items():
        print(f"Socio n°{socio_numero}: {datos_socio['nombre']}- Fecha de Ingreso: {datos_socio['fecha_ingreso']} - Cuota al día: {'Sí' if datos_socio['cuota_al_dia'] else 'No'}")