import funciones_tp7

#Ejercicio 1
list_num=[]

while True:
    num=int(input("Ingrese un número (ingrese 0 para terminar): "))
    if num==0:
        break
    else:
        list_num.append(num)

print(f"Lista Ingresada: {list_num}")
print(f"Lista Ordenada: {funciones_tp7.bubble_Sort(list_num)}")

#Ejercicio 2
list_words=[]

while True:
    word=input("Ingrese una palabra (ingrese x para terminar): ").lower()
    if word=="x":
        break
    else:
        list_words.append(word)

print(f"Lista Ingresada: {list_words}")
print(f"Lista Ordenada Alfabeticamente: {funciones_tp7.selection_Sort(list_words)}")

#Ejercicio 3
books=[
    {
        "titulo": "Titán del gol y de la vida",
        "autor": "Martin Palermo",
        "año_publicacion": 2012
    },
    {
        "titulo": "Martin Fierro",
        "autor": "José Hernandez",
        "año_publicacion": 1872
    },
    {
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "año_publicacion": 1943
    }
]
while True:
    option=input("Como desea ordenar los libros? (ingrese el numero de la opcion) \n"
                "1) Titulo                       \n"
                "2) Autor                        \n"
                "3) Año de publicacion           \n"
                "--------------------------------\n")
    
    if option=="1":
        funciones_tp7.title_Order(books)
        print("Titulos Ordenados Alfabeticamente: ")
        for book in books:
            print(book["titulo"])
        break
    elif option=="2":
        funciones_tp7.author_Order(books)
        print("Autores Ordenados Alfabeticamente: ")
        for book in books:
            print(book["autor"])
        break
    elif option=="3":
        funciones_tp7.year_Order(books)
        print("Ordena por año de publicacion: ")
        for book in books:
            print(book["año_publicacion"])
        break
    else:
        print("La opcion ingresada no es valida")

#Ejercicio 4
list_words=[]
while True:
    word=input("Ingrese una palabra (ingrese x para terminar): ").lower()
    if word=="x":
        break
    else:
        list_words.append(word)
print(f"Lista Ingresada: {list_words}")
print(f"Lista Ordenada según la longitud de las palabras:\n"
    f"{funciones_tp7.insert_Sort(list_words)} \n")

#Ejercicio 5
list_num=[]
while True:
    num=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if num == 0:
        break
    else:
        list_num.append(num)
print(f"Lista Ingresada: {list_num}")
print(f"Lista Ordenada en forma Descendente: {funciones_tp7.bubble_Sort_Des(list_num)}")

#Ejercicio 6
list_num=[]
while True:
    num=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if num == 0:
        break
    else:
        list_num.append(num)
print(f"Lista Ingresada: {list_num}")
print(f"Lista Ordenada en forma Ascendente: {funciones_tp7.count_Order(list_num)}")

#Ejercicio 7
list_elements=["Tortuga","Mapache",15,19,"Gato",9,"Canario",6]
funciones_tp7.order_Elements(list_elements)

#Ejercicio 8
list_num=[]
while True:
    num=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if num ==0:
        break
    else:
        list_num.append(num)
print(f"Lista Ingresada: {list_num}")
print(f"Lista Ordenada: {funciones_tp7.merge_Sort(list_num)}")