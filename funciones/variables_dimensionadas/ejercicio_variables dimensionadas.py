import funciones_vd
#Ejercicio 1
datos_viajantes = [('Pedro Martinez',45532785,'Manchester'),('Gonzalo Ramos', 48563217, 'Lisboa'), ('Roger Martinez', 47553246, 'Chubut')]
datos_pais = [('Manchester','Inglaterra'), ('Lisboa','Portugal'),('Chubut','Argentina')]

opcion = input("Que desea realizar:\n 1)Agregar pasajeros a la lista de viajeros.\n 2)Agregar ciudades a la lista de ciudades.\n 3)Dado el DNI de un pasajero saber a que ciudad viaja.\n 4)Dada una ciudad, mostar cuantos pasajeros viajan a esa ciudad.\n 5)Dado el DNI de un pasajero, ver a qué país viaja.\n 6)Dado un país, mostrar cuántos pasajeros viajan a ese país. \n 7)Salir.\n")


if(opcion == "1"):
    datos_viajantes.append(funciones_vd.agregar_pasajero())
    print(datos_viajantes)
elif(opcion == "2"):
    datos_pais.append(funciones_vd.agregar_ciudad())
    print(datos_pais)
elif(opcion == "3"):
    funciones_vd.buscar_destino_por_dni(datos_viajantes)
elif(opcion == "4"):
    funciones_vd.contar_pasajeros_ciudad(datos_viajantes)
elif(opcion == "5"):
    funciones_vd.buscar_pais_dni(datos_viajantes,datos_pais)
elif(opcion == "6"):
    funciones_vd.contar_pasajeros_pais(datos_pais)
elif(opcion == "7"):
    print("Hasta luego!")

##Ejercicio 2