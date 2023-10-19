import random
def buscar_eliminar_num(num_buscar,num):
    for i in num:
        if (i == num_buscar):
            num.remove(num_buscar)
            print("El número que se buscaba se encontro y se elimino")
        else:
            continue

def sumar_elementos(num):
    suma_num = 0

    for i in num:
        suma_num = suma_num + i
    print(f"La suma de los números ingresados es: {suma_num}")

def nueva_lista(num_aux, num_nuevos, num):
    for i in num: 
        if (i < num_aux ):
            num_nuevos.append(i)

    print("Array nuevo")
    print(num_nuevos)

def generar_listas_tuplas(num):
    list_tupla = []
    for i in num:
        cont = 0
        for j in num:
            if (i == j ):
                cont += 1
        list_tupla.append((i,cont))
    
    print(list_tupla)

##Ejercicio 6
def mostrar_alumnos(alumnos_primario,alumnos_secundario):
    print("Alumnos primario")
    for i in alumnos_primario:
        print(i)

    print("Alumnos secundario")
    for j in alumnos_secundario:
        print(j)

def alumnos_repetidos(alumnos_primario, alumnos_secundario):
    alumnos_repetidos = []

    for i in alumnos_primario:
        for j in alumnos_secundario:
            if (i == j):
                alumnos_repetidos.append(i)
    
    print(alumnos_repetidos)

# def alumnos_no_repetidos(alumnos_primario, alumnos_secundario):
#     alumnos_no_repetidos = []
#     for i in alumnos_primario:
#         for j in alumnos_secundario:
#             if (i != j):
#                 alumnos_no_repetidos.append(j)
#     print(alumnos_no_repetidos)
            
def games(goals_team, rows, columns):
   
    for i in range(rows-1):
        print(f"Partido {i+1}:")
        for j in range(columns-1): 
            print(f"{i+1} vs {j+1}")
            if( i == j):
                goals_team [i][j] = 0
            else:
                goals_team[i][j] = random.randint(0,5)
                goals_team[j][i] = random.randint(0,5)

    
    for rows in goals_team:
        for elemento in rows:
            print(elemento, end=" ")  # Imprimir cada elemento en una fila separada por tabulaciones
        print() 

def resultado_equipos(goals_team, rows, columns):
    games_result_team =[]
    points_obt = []
    
   
    for i in range(rows-1):
        games_win = 0
        games_lose = 0
        games_tied = 0
        points = 0
        for j in range(columns-1): 
            if (goals_team[i][j] > goals_team[j][i]):
                games_win += 1
            elif (goals_team[i][j] < goals_team[j][i]):
                games_lose += 1
            else:
                games_tied += 1
            
            
        if (games_win > 0):
            points = points + games_win * 3
                
        if (games_tied > 0):
            points = points + games_tied 

        points_obt.append(points)
        games_result_team.append((games_win,games_tied,games_lose))
        
    ##Muestra el resultado de cada equipo en los distintos partidos
    print("(victoria,empate,derrota)")
    k=1
    for i in games_result_team:
        print(f"Equipo {k}: ")
        print(i)
        k += 1

    ##Muestra los puntos obtenidos por equipo
    m = 1
    print("Puntos obtenidos: ")
    for l in points_obt:
        print(f"Equipo {m}: ")
        print(l)
        m += 1



def goal_diference(goals_team,rows,columns):
    goals =[]
   
    for i in range(rows-1):
        diference_goal = 0
        goal_against = 0
        goal_favor = 0
        for j in range(columns-1): 
            if(i != j):
                if (goals_team[i][j] > 0):
                    goal_favor = goal_favor + goals_team[i][j]
                
                if (goals_team[j][i] > 0):
                    goal_against = goal_against + goals_team[j][i]
         
        diference_goal = goal_favor - goal_against
        goals.append((goal_favor,goal_against, diference_goal))

    print(" ")
    print("(goles a favor, goles en contra, diferencia de gol)")
    k = 1
    for i in goals:
        print(f"Equipo {k}")
        print(i)
        k += 1

