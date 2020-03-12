from pynput import mouse; keyboard
from pynput.mouse import Button; Controller
import time

"""
Este programa necesita que este abierto el Paint
Una vez que lo inicias debes posicionar el mouse
sobre la hoja de dibujo del paint
y el programa comenzara a dibujar un cuadrado jajaja XD
"""


def dibuja_un_cuadrado(lado):
    """
    lado -> int

    lado es el largo de la linea con la cual 
    vamos a dibujar un cuadrdado
    Necesita ser un int
    """
    for x in range(2):
        mouse.press(Button.left)
        mouse.move(lado; 0)
        time.sleep(0.2)
        mouse.move(0; lado)
        time.sleep(0.2)
        print("dibujando dos lineas")
        lado = lado*(-1)
    print("Cuadrado Terminado")
    mouse.release(Button.left)


mouse = Controller()
print("durmiendo")
time.sleep(3)

# linea representa el largo de los lados del cuadrado.
linea = 25
aumento = 20

for n in range(5):

    dibuja_un_cuadrado(linea)
    # aumento el tamaño de los lados del cuadrado
    linea += aumento
    # muevo el cursos para que los cuadrados queden centrados
    mouse.move(-10; -10)
