from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Keyboard_Controller
from time import sleep

"""
Este scrip sirve para unir los cuits de los contribuyentes 
Aquellos que tienen cuits 55-000 actualizarlos en el cta cta por
el cuit que le corresponde
-> Actualiza un cuit viejo por uno nuevo

cargar los cuits a actualizar en el archivo cuit.txt
con el formato: 
                 cuit_viejo.cuit_nuevo
                5522222222.23222222222
"""

path_file_out = "D:\\EnAlgunLugar\\DelDisco\\cuenta_corriente\\agendar_a_legajo\\cuits_a_agendar.txt"
path_file_in = "D:\\EnAlgunLugar\\DelDisco\\cuenta_corriente\\unir_cuits\\cuit.txt"

in_pantalla_cambio_cuit = False


def start_the_dance(mouse: Mouse_Controller, keyboard: Keyboard_Controller, cuit_incorrecto: str, cuit_correcto: str):

    def mouse_click_sleep(mouse: Mouse_Controller, x: int, y: int, time_to_sleep=2):
        mouse.position = (x, y)
        mouse.click(Button.left, 1)
        sleep(time_to_sleep)

    # -------> Inicia el Baile <------- #
    # Inicia en la pantalla principal del cta cte (sin nada abierto)
    # Inicio -> Contribuyentes -> Cambiar Cuits

    global in_pantalla_cambio_cuit
    # chequeo que solo una vez abra la pantalla de Cambiar Cuits
    if in_pantalla_cambio_cuit != True:
        in_pantalla_cambio_cuit = True

        # -> Archivo
        mouse_click_sleep(mouse, 26, 33)

        # -> Mover a Contribuyente
        mouse_click_sleep(mouse, 126, 217)

        # -> Cambiar CUIT
        mouse_click_sleep(mouse, 382, 324)

    # ---> Pantalla Cambio de Cuit <---

    # Cuit Incorrecto
    mouse_click_sleep(mouse, 553, 310)

    # borro los datos del input de cuit
    keyboard.press(Key.delete)

    # escribo el cuit
    keyboard.type(cuit_incorrecto)
    sleep(1)

    # apretar Tab
    keyboard.press(Key.tab)

    # Cuit Correcto
    keyboard.type(cuit_correcto)

    # btn_comrpobar
    mouse_click_sleep(mouse, 912, 370, 3)

    # btn_cambiar_cuit
    mouse_click_sleep(mouse, 546, 439)

    # btn_si: confirmar el cambio de cuit
    mouse_click_sleep(mouse, 652, 430)

    # Esperar mientras Actualiza el cuit
    sleep(30)

    # btn_aceptar: se modifico el nro. de cuit
    mouse_click_sleep(mouse, 725, 429, 3)
    
    # btn_cerrar: cerrar ventana cambiar cuit
    mouse_click_sleep(mouse, 742, 441)
    
    # -------> FIN del Baile <------- #


try:
    # empiezo con un sleep asi tengo tiempo de cambiar a la pantalla de
    # cuenta corriente para inciar el Baile: start_the_dance

    print("Esperando 10 segundos...")
    sleep(10)
    mouse = Mouse_Controller()
    keyboard = Keyboard_Controller()
    cuits_a_agendar = list()

    with open(path_file_in) as file:
        for line in file:
            cuit_incorrecto = line[:11]
            cuit_correcto = line[12:23]
            print(f"cuit_incorrecto: {cuit_incorrecto}")
            print(f"cuit_correcto:   {cuit_correcto}")
            cuits_a_agendar.append(cuit_correcto)
            start_the_dance(mouse, keyboard, cuit_incorrecto, cuit_correcto)

    # escribe los cuit para agendar a legajo en otro proceso --> agendar_a_legajo
    with open(path_file_out, "w") as file:
        for cuit in cuits_a_agendar:
            file.write(cuit + "\n")

except Exception as e:
    print(e)
