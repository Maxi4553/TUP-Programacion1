import math
#Ejercicio 1
def cant_digitos(num):
    digitos = len(num)
    print(f"La cantidad de digitos que tiene el número {num} es {digitos}")

#Ejercicio 2
def potencia_de_otro(base,exponent):
    result = math.pow(base,exponent)

    if (result % exponent == 0):
        return True
    else:
        return False
    
##Ejercicio 3
def position(phrase,b,pos=0):
    if pos == len(phrase):
        return []  

    if phrase.startswith(b, pos):
        return [pos] + position(phrase, b, pos + 1)
    else:
        return position(phrase, b, pos + 1)
    
##Ejercicio 4
def even(num):
    if num == 0:
        return True  
    else:
        return odd(num - 1)

def odd(num):
    if num == 0:
        return False  
    else:
        return even(num - 1) 
    
##Ejercicio 5
def max_list_num(array_num, i, max_num):
    if((len(array_num)-1) >= i):
        if(array_num[i] > max_num):
            max_num = array_num[i]
        return max_list_num(array_num, i+1, max_num)
    else:
        return max_num
    
##Ejercicio 6
def repeat_num(array_num, num_repeats):
    if not array_num:
        return []
    current_element = array_num[0]
    repeated_elements = [current_element] * num_repeats
    return repeated_elements + repeat_num(array_num[1:], num_repeats)

##Ejercicio 7 
def sum_recursiva(n,p):
    if (n>1):
        return (p*n) + sum_recursiva(n-1,p)
    elif(n <=0):
        return ("n no puede valer ni ser menor a 0")
    elif n == 1: 
        return p
    
##Ejercicio 8
def calculate_pascal(row, column):
    if column == 0 or column==row:
        return 1
    else:
        return calculate_pascal(row - 1, column - 1) + calculate_pascal(row - 1, column)
    

##Ejercicio 9 
def combinations(char,n,built_chain=""):
    if n==0:
        print(built_chain)
        return  
    else:
        for i in char:
            combinations(char,n-1,built_chain+i)

##Ejercicio 10
def sheet_measurement(n):
    if n==0:
        return(841,1189)
    previous_width, previous_length = sheet_measurement(n-1)
    if n % 2 == 1:
        return (previous_length, previous_width // 2)
    else:
        return (previous_width // 2, previous_length)
