import pytest
from funciones import *

##Ejercicio 1
# @pytest.mark.parametrize("dni, res",[
#     ("45532469","Su dni fue ingresado correctamente"),
#     ("45532769","Su dni fue ingresado correctamente"),
#     ("44432465","Su dni fue ingresado correctamente"),
#     ("444585","El dni debe contener entre 7 y 8 digitos"),
#     ("44432465","Su dni fue ingresado correctamente"),
# ])
# def test_dni(dni, res):
#     assert verificar_dni(dni) == res

##Ejercicio 2 
# @pytest.mark.parametrize("string, cont ,res",[
#     ("M A X I M O", 6,),
#     ("CASA", 4,),
#     (" P E RR O", 5, ),
# ])
# def test_string(string,cont, res):
#     assert long_string(string,cont) == res

##Ejercicio 3
# @pytest.mark.parametrize("nombre, apellido, dni, id, res",[
#     ("Pedro Alfredo","Gomez","45532469", "Pedro455","Socio Cargado correctamente"),
#     ("Pedro","Estebam","45532478", "Pedro455", "Socio Cargado correctamente"),
#     ("Alfredo","Gomez","45532469", "Alfredo455", "Socio Cargado correctamente"),
#     ("Mariano","Perez","45532468", "Mariano455", "Socio Cargado correctamente"),
#     ("Ricardo Alberto","Diaz","24258963", "Ricardo455", "Socio Cargado correctamente"),
# ])
# def test_socio(nombre,apellido,dni,id, res):
#     assert socios_club(nombre,apellido,dni,id) == res

##Ejercicio 4
# @pytest.mark.parametrize("num1,num2,res",[
#     (6,2,"Los números ingresados son multiplos entre si"),
#     (2,6,"Los números ingresados no son multiplos entre si"),
#     (3,8,"Los números ingresados no son multiplos entre si"),
#     (4,2,"Los números ingresados son multiplos entre si"),
#     (12,6,"Los números ingresados son multiplos entre si"),
# ])
# def test_multiplo(num1,num2,res):
#     assert numero_multiplo(num1, num2) == res

##EJercicio 5
# @pytest.mark.parametrize("temp_min, temp_max, res ",[
#     (12,20,16),
#     (18,27,22.5),
#     (25,17,"La temperatura minima no puede ser mayor que la máxima"),
#     (22,30,26),
#     (27,11,"La temperatura minima no puede ser mayor que la máxima"),

# ])
# def test_temp(temp_min, temp_max, res):    
#     assert temp_media(temp_min, temp_max) == res

##EJercicio 6 
# @pytest.mark.parametrize("text, res",[
#     ("Perro", " P e r r o"),
#     ("salto en largo", " s a l t o   e n   l a r g o"),
#     ("monte", " m o n t e"),
#     ("python funciones", " p y t h o n   f u n c i o n e s"),
#     ("sabado, me voy para el baile", " s a b a d o ,   m e   v o y   p a r a   e l   b a i l e")
# ])
# def test_text_espacios(text, res):
#     assert cadena_espacios(text) == res

##Ejercicio 7
# @pytest.mark.parametrize("num, res", [
#     ([2,5,6,9,22,4,7,6],(22,2)),
#     ([2,12,6,9,1,4,7,6],(12,1)),
#     ([12,5,6,9,1,4,22,6],(22,1)),
#     ([2,5,6,9,1,12,7,6],(12,1)),
#     ([13,20,6,9,5,19,12,6],(20,5)),
# ])
# def test_num_menor_mayor(num,res):
#     assert mayor_menor_num(num) == res

##Ejercicio 8

# @pytest.mark.parametrize("radio, res",[
#     (5, (78.5398,31.4159)),
#     (15, (706.8583,94.2478)),
#     (12.7, (506.7075,79.7965)),
#     (13.68, (587.9252,85.954)),
#     (9, (254.469,56.5487)),
# ])
# def test_perim_radio(radio, res):
#     assert area_perim_circunferencia(radio) == res

##Ejercicio 9 
# @pytest.mark.parametrize("usuario,contra, res",[
#     ("usuario1","asdasd", "Verdadero"),
#     ("usuario1","asdasd", "Verdadero"),
#     ("Usuario2","asdasd", "Vuelva a intentarlo"),
#     ("Usuario2","asdasg", "Vuelva a intentarlo"),
#     ("usuario1","asdasg", "Vuelva a intentarlo, contraseña incorrecta"),
# ])
# def test_login(usuario,contra, res):
#     assert login(usuario, contra) == res

##Ejercicio 10

##Ejercicio 14
# @pytest.mark.parametrize("num ,res",[
#     (2,"El número ingresado es primo"),
#     (4,"El número ingresado no es primo"),
#     (7,"El número ingresado es primo"),
#     (12,"El número ingresado no es primo"),
#     (29,"El número ingresado es primo"),
# ])
# def test_primo(num,res):
#     assert num_primo(num) == res