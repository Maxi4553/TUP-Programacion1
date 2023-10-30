class Person:

    def __init__(self):
        self.__name = ""
        self.__age = 0 
        self.__dni = ""
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_at):
        self.__name = new_at

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,new_at):
        self.__age = new_at
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,new_at):
        self.__dni = new_at 
    
    def mostrar(self):
        print(f"Nombre: {self.__name}\nDNI: {self.__dni} \nEdad: {self.__age} ")

    def mayor_edad(self):
        if (self.__age >= 18):
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


class Cuenta:
    def __init__(self, headline, quantity=0.0):
        self.headline = headline
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("La cantidad no puede ser negativa")

    def show(self):
        print(f"Titular: {self.headline}")
        print(f"Cantidad: {self.get_quantity()}")

    def ingresar(self, quantity):
        if quantity >= 0:
            self.__quantity += quantity
        else:
            print("No se puede ingresar una cantidad negativa")

    def retirar(self, quantity):
        self.__quantity -= quantity

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {mayor}")

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print(f"Contacto {nombre} añadido a la agenda.")

    def lista_de_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                print("-------------------")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto encontrado:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                return
        print(f"No se encontró un contacto con el nombre {nombre}.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto {nombre} actualizado.")

    def menu(self):
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.añadir_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.lista_de_contactos()
            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre a editar: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)
            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
