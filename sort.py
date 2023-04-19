from pyray import *
import time
import random

ancho = 1500
alto = 800
cant_element = int(input("Ingrese la cantidad de elementos : "))
space = (ancho/(cant_element+2))/5

while cant_element <= 0:
    print("\n¡¡¡ERROR Ingrese un numero mayor a cero !!!")
    cant_element = int(input("Ingrese la cantidad de elementos : "))

#ancho de cada barra
ancho_b = ancho / (cant_element + 2)

# Creamos una lista vacia
element = []

num = 20
lista_apoyo = []
for i in range(cant_element):
    element.append(random.randint(100, 1000))
    lista_apoyo.append(element[i])
    print("elemento ", i, " : ", element[i])

lista_apoyo.sort(key=None, reverse=False)

#Iniciamos una ventana
init_window(ancho, alto, "SORT")

def graficar():
    for i in range(cant_element):
        if i == 0:
            draw_rectangle(int((ancho/(cant_element+2))/5), alto-element[i], int(ancho/(cant_element+2)), element[i], GRAY)
        else:
            draw_rectangle(int(((ancho/(cant_element+2)) + space)*i), alto-element[i], int(ancho/(cant_element+2)), element[i], GRAY)

def bubble_sort():
    while element != lista_apoyo:
        for i in range(cant_element):
            clear_background(BLACK)
            draw_rectangle(int(((ancho/(cant_element+2)) + space)*(i+1)), alto-element[i], int(ancho/(cant_element+2)), element[i], WHITE)
            if i <= cant_element-3 and element[i] > element[i+1]:
                var_apoyo = element[i]
                element[i] = element[i+1]
                element[i+1] = var_apoyo
            clear_background(BLACK)
            graficar()
            end_drawing()
    draw_text("HOLA", 30, 30, 50, RED)

condition = -1

while not window_should_close():
    clear_background(BLACK)
    graficar()
    if is_key_pressed(KEY_SPACE) or condition == 0:
        condition = 0
        while condition == 0:
            bubble_sort()
    end_drawing()
close_window()