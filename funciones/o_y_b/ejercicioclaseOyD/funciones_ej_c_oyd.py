def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            # Compara el elemento actual con el siguiente
            if num_list[j] > num_list[j + 1]:
                # Realiza el intercambio
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                intercambiado = True

        # Si no hubo intercambios en este pase, la lista ya está ordenada.
        if not intercambiado:
            break
    print(num_list)

def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la parte no ordenada de la lista.
        min_index = i
        for j in range(i + 1, n):
            if num_list[j] < num_list[min_index]:
                min_index = j

        # Intercambia el elemento mínimo con el primer elemento de la parte no ordenada.
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

    print(num_list)

def inser_sort(num_list):

    for i in range(1, len(num_list)):
        # Guarda el valor actual para su posterior inserción.
        valor_actual = num_list[i]
        posicion = i

        # Mueve los elementos mayores que el valor actual hacia adelante.
        while posicion > 0 and num_list[posicion - 1] > valor_actual:
            num_list[posicion] = num_list[posicion - 1]
            posicion -= 1

        # Inserta el valor actual en su posición correcta.
        num_list[posicion] = valor_actual
    print(num_list)

def merge_sort(num_list):
      
      if len(num_list) > 1:
        mitad = len(num_list) // 2
        mitad_izquierda = num_list[:mitad]
        mitad_derecha = num_list[mitad:]

        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                num_list[k] = mitad_izquierda[i]
                i += 1
            else:
                num_list[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            num_list[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            num_list[k] = mitad_derecha[j]
            j += 1
            k += 1
        print(num_list)