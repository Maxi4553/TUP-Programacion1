from Motocicleta import Motocicleta

motorcycle_one = Motocicleta("Gris", "A404664", 10, 2, "Honda", 2023, "25/02/2023", 150, 500 )
motorcycle_two = Motocicleta("Azul", "A668515", 10, 2, "Susuki", 2012, "23/04/2012", 175, 250 )

motorcycle_one.arrancar()
motorcycle_one.detener()
motorcycle_one.detener()

print(f"El color es {motorcycle_one.color}")

motorcycle_one.mostrar_color()
motorcycle_one.precio = 10000

print(f"El precio de la motocicleta {motorcycle_one.brand} {motorcycle_one.model} es de ${motorcycle_one.precio}.")

print(motorcycle_one.precio_one())

motorcycle_one.precio_one()
motorcycle_two.precio_one()

