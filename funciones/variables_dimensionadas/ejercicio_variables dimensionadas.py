import funciones_vd
##Ejercicio 1
# datos_viajantes = [('Pedro Martinez',45532785,'Manchester'),('Gonzalo Ramos', 48563217, 'Lisboa'), ('Roger Martinez', 47553246, 'Chubut')]
# datos_pais = [('Manchester','Inglaterra'), ('Lisboa','Portugal'),('Chubut','Argentina')]

# opcion = input("Que desea realizar:\n 1)Agregar pasajeros a la lista de viajeros.\n 2)Agregar ciudades a la lista de ciudades.\n 3)Dado el DNI de un pasajero saber a que ciudad viaja.\n 4)Dada una ciudad, mostar cuantos pasajeros viajan a esa ciudad.\n 5)Dado el DNI de un pasajero, ver a qué país viaja.\n 6)Dado un país, mostrar cuántos pasajeros viajan a ese país. \n 7)Salir.\n")


# if(opcion == "1"):
#     datos_viajantes.append(funciones_vd.agregar_pasajero())
#     print(datos_viajantes)
# elif(opcion == "2"):
#     datos_pais.append(funciones_vd.agregar_ciudad())
#     print(datos_pais)
# elif(opcion == "3"):
#     funciones_vd.buscar_destino_por_dni(datos_viajantes)
# elif(opcion == "4"):
#     funciones_vd.contar_pasajeros_ciudad(datos_viajantes)
# elif(opcion == "5"):
#     funciones_vd.buscar_pais_dni(datos_viajantes,datos_pais)
# elif(opcion == "6"):
#     funciones_vd.contar_pasajeros_pais(datos_pais)
# elif(opcion == "7"):
#     print("Hasta luego!")

##Ejercicio 2
compras = [
    ('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'),
    ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
    ('Nuria Costa', 12, 800.0, 'Calle 1 - 456'),
    ('Laura Perez', 15, 1500.75, 'Calle 3 - 123')
]

domicilios = funciones_vd.obtener_domicilios_factura(compras)
print(domicilios)

#Ejercicio 3

while True:
    print("\nOpciones:")
    print("1. Informar cantidad de socios")
    print("2. Registrar que un socio ha pagado todas las cuotas adeudadas")
    print("3. Modificar la fecha de ingreso de socios")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")
    
    opcion = input("Elija una opción: ")
    
    if (opcion == "1"):
        funciones_vd.informar_cantidad_socios()
    elif (opcion == "2"):
        numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
        funciones_vd.pagar_cuotas(numero_socio)
    elif (opcion == "3"):
        funciones_vd.modificar_fecha_ingreso()
    elif (opcion == "4"):
        nombre_apellido = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
        funciones_vd.dar_de_baja(nombre_apellido)
    elif (opcion == "5"):
        funciones_vd.imprimir_listado_socios()
    elif (opcion == "6"):
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")