class Motocicleta:
    motor = False

    def __init__(self, color, patent, fuel_liter, number_wheels, brand, model, date_manufacturing, speed, weight):

        self.color = color 
        self.patent = patent
        self.fuel_liter =  fuel_liter
        self.number_wheels = number_wheels
        self.brand = brand
        self.model = model
        self.date_manufacturing = date_manufacturing
        self.speed = speed
        self.weight = weight

    def arrancar(self):
        if (self.motor == False):
            print("Motor arrancado")
            self.motor = True
        else:
            print("El motor ya esta encendido")
    
    def detener(self):
        if (self.motor == True):
            print("El motor se detuvo")
            self.motor = False
        else:
            print("El motor ya esta detenido")

    def mostrar_color(self):
        print(f"El color de la moto es {self.color} desde un metodo")

    def precio_one(self):
        return self.precio