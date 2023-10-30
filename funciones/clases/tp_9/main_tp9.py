##Ejercicio 1
# from person import Person

# person_one = Person()

# person_one.name = "Juan Roman Riquelme"
# person_one.age = 20
# person_one.dni = "45532559"


# print(f"{person_one.name} tiene {person_one.age} años, y su DNI es {person_one.dni}")

# person_one.mostrar()
# person_one.mayor_edad()

# from person import Cuenta
# cuenta1 = Cuenta("Juan", 1000.0)
# cuenta1.show()

# cuenta1.ingresar(500.0)
# cuenta1.show()

# cuenta1.retirar(200.0)
# cuenta1.show()

# cuenta1.retirar(1500.0) 
# cuenta1.show()

# from person import Triangulo
# def ingresar_datos_triangulo():
#     lado1 = float(input("Ingrese el valor del primer lado: "))
#     lado2 = float(input("Ingrese el valor del segundo lado: "))
#     lado3 = float(input("Ingrese el valor del tercer lado: "))
#     return lado1, lado2, lado3

# if __name__ == "__main__":
#     lado1, lado2, lado3 = ingresar_datos_triangulo()
#     triangulo = Triangulo(lado1, lado2, lado3)

#     triangulo.imprimir_lado_mayor()
#     tipo = triangulo.determinar_tipo()
#     print(f"El triángulo es de tipo: {tipo}")

from person import Contacto,Agenda

agenda = Agenda()
agenda.menu()
