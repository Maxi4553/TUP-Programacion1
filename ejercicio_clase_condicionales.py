fecha_actual = input("Ingrese la fecha actual(dia/DD/MM): ")
fecha = fecha_actual.split(" ")
dias = fecha[0].upper() 
dia = int(fecha[1]) 
mes = int(fecha[2]) 

if (dias == "LUNES") or (dias == "MARTES") or (dias == "MIERCOLES") or (dias == "JUEVES") or (dias == "VIERNES"): 
    if (dia >= 1 and dia <= 31): 
        if(mes >= 1 and mes <= 12): 
            print("Acceso correcto")
            if (dias == "LUNES") or (dias == "MARTES") or (dias == "MIERCOLES"): 
                examenes = input("¿Hubo examenes? ")
                if examenes.upper() == "SI": 
                    alumnos_rindieron = int(input("¿Cuantos alumnos rindieron? "))
                    alumnos_aprobados =  int(input("¿Cuantos alumnos aprobaron? "))
                    procentaje_aprobados = (alumnos_aprobados*100)/alumnos_rindieron
                    print(f"El procentaje de aprobados es {procentaje_aprobados}%")
                else:
                    print("No se rindieron examenes ")
            elif (dias == "JUEVES"):
                asistencia = int(input("Ingrese el porcentaje de asistencia: "))
                if(asistencia > 50):
                    print("Asisitio a la mayoria")
                else:
                    print("No asistio a la mayoria")
            elif(dia == 1 and (mes == 1 or mes == 7)):
                print("Comienzo de nuevo ciclo")
                cant_alumnos = int(input("Cuantos alumnos ingresaron: "))
                arancel_por_alumno = int(input("Ingrese el arancel por alumno: "))
                arancel_total = cant_alumnos * arancel_por_alumno

                print(f"El arancel total es: {arancel_total}")
            else:
                print("")
        else:
            print("Acceso incorrecto")  
    else:
        print("Acceso incorrecto")        
else:
    print("Acceso incorrecto")