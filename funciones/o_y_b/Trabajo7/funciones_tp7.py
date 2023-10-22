##Ejercicio 1
def bubble_Sort(list_num):
    for i in range(len(list_num)):
        for j in range(0,len(list_num)-i-1):
            if list_num[j] > list_num[j+1]:
                list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
    return list_num

##Ejercicio 2
def selection_Sort(list_words):
    for i in range(len(list_words)-1):
        minor=list_words[i]
        pos=i
        for j in range(i+1,len(list_words)):
            if list_words[j]<minor:
                minor=list_words[j]
                pos=j
        if pos!=i:
            tmp=list_words[i]
            list_words[i]=list_words[pos]
            list_words[pos]=tmp
    return list_words

##Ejercicio 3
def title_Order(books):
    for i in range(len(books)):
        for j in range(0,len(books)-i-1):
            if books[j]["titulo"] > books[j+1]["titulo"]:
                books[j], books[j+1] = books[j+1], books[j]
    return books

def author_Order(books):
    for i in range(len(books)):
        for j in range(0,len(books)-i-1):
            if books[j]["autor"] > books[j+1]["autor"]:
                books[j], books[j+1] = books[j+1], books[j]
    return books

def year_Order(books):
    for i in range(len(books)):
        for j in range(0,len(books)-i-1):
            if books[j]["año_publicacion"] > books[j+1]["año_publicacion"]:
                books[j], books[j+1] = books[j+1], books[j]
    return books

##Ejercicio 4
def insert_Sort(list_word):
    for i in range(len(list_word)):
        aux = list_word[i]
        j = i - 1
        while j >= 0 and len(aux) < len(list_word[j]):
            list_word[j + 1] = list_word[j]
            j-=1            
        list_word[j + 1] = aux
    return list_word

##Ejercicio 5
def bubble_Sort_Des(list_num):
    for i in range(len(list_num)):
        for j in range(0,len(list_num)-i-1):
            if list_num[j] < list_num[j+1]:
                list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
    return list_num

##Ejercicio 6
def count_Order(list_num):
    sorted_list = []

    if not list_num:
        return list_num
    min_val = min(list_num)
    max_val = max(list_num)

    count_arr = [0] * (max_val - min_val + 1)

    for num in list_num:
        count_arr[num - min_val] += 1

    for i, count in enumerate(count_arr):
        sorted_list.extend([i + min_val] * count)

    return sorted_list

##Ejercicio 7
def order_Elements(elements):
    list_num=[]
    list_word=[]
    for i in elements:
        if type(i)==int:
            list_num.append(i)
        elif type(i)==str:
            list_word.append(i)
    print(f"Lista de numeros ordenada: {selection_Sort(list_num)}")
    print(f"Lista de palabras ordenada alfabeticamente: {selection_Sort(list_word)}")

##Ejercicio 8
def merge_Sort(list_num):
    if len(list_num) > 1:
        mid = len(list_num) // 2
        left_half = list_num[:mid]
        right_half = list_num[mid:]

        merge_Sort(left_half)
        merge_Sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_num[k] = left_half[i]
                i += 1
            else:
                list_num[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list_num[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list_num[k] = right_half[j]
            j += 1
            k += 1
    return list_num
