from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Keyboard_Controller
from time import sleep
import time


start = time.perf_counter()  # para medir cuanto tiempo demora

# path_file_out = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\unir_cuits\\procesados.txt"
path_file_in = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\agendar_a_legajo\\cuits_a_agendar.txt"
in_pantalla_agenda = False


def start_the_dance(mouse: Mouse_Controller, keyboard: Keyboard_Controller, cuit: str):

    def mouse_click_sleep(mouse: Mouse_Controller, x: int, y: int, clicks=1, time_to_sleep=1):
        mouse.position = (x, y)
        mouse.click(Button.left, clicks)
        sleep(time_to_sleep)

    # -------> Inicia el Baile <------- #
    # Pantalla de Inicio: Cuenta Corrientes
    #
    # Agenda -> Nuevo Registro
    global in_pantalla_agenda

    # Chequeo si esta en la pantalla para agendar contribuyentes.
    #   - si SI, no hago nada y sigo agendando contribuyentes
    #   - si NO, abro la pantalla para agendar contribuyentes una vez
    if in_pantalla_agenda != True:
        in_pantalla_agenda = True

        # btn_agenda
        mouse_click_sleep(mouse, 845, 32)

        # Nuevo Registro
        mouse_click_sleep(mouse, 881, 54, time_to_sleep=2)

    # Pantalla: Alta de registro Agenda del Contribuyente
    #
    # input_contribuyente: ingreso cuit
    mouse_click_sleep(mouse, 411, 112)

    # borro los dadtos del input de cuit
    keyboard.press(Key.delete)
    sleep(0.3)

    # escribo el cuit
    keyboard.type(cuit)
    sleep(1)
    keyboard.press(Key.enter)
    sleep(1)
    # dropbox_actuacion: posicionar el mouse
    mouse_click_sleep(mouse, 702, 441, time_to_sleep=2)

    # presionar la "D" 8 veces para elegir: Documentacion Recibida
    for _ in range(8):
        keyboard.press("d")
        keyboard.release("d")
        sleep(0.5)
    keyboard.press(Key.enter)
    sleep(1)

    # dropbox_deriva_a: posicionar el mouse en
    mouse_click_sleep(mouse, 652, 477, time_to_sleep=2)

    # elegir depto Legajo, presionando la "D" 49 veces
    for _ in range(49):
        keyboard.press("d")
        keyboard.release("d")
        sleep(0.5)
    keyboard.press(Key.enter)
    sleep(1)

    # btn_confirmar: Confirmar
    mouse_click_sleep(mouse, 1109, 415)

    # btn_aceptar: Datos Agregados
    mouse_click_sleep(mouse, 702, 428)

    # muevo la posicion del cursor al input de numero
    # para que luego funcione al ingresar el cuit siguiente
    mouse_click_sleep(mouse, 789, 441)
    
    # btn_cerrar: cerrar vetana Agenda de Contribuyente
    mouse_click_sleep(mouse, 1110, 657) 

# -------> FIN del Baile <------- #


try:
    # empiezo con un sleep asi tengo tiempo de cambiar a la pantalla de
    # cuenta corriente para inciar el Baile: start_the_dance

    print("Durmiendo 10 segundos")
    sleep(10)
    mouse = Mouse_Controller()
    keyboard = Keyboard_Controller()
    # procesados = list()

    with open(path_file_in) as file:
        for line in file:
            # otro metodo de obtener los cuits del archivo
            # print(f"cuit: {line.split()[0]}")
            # cuit = line[:11]
            print(f"cuit: {line[:11]}")
            start_the_dance(mouse, keyboard, line[:11])  # line[:11] = cuit

except Exception as e:
    print(e)

finish = time.perf_counter()

# muestra cuanto tiempo demoro en realizar toda la tarea
print(f"Tarea terminada en {round(finish-start, 2)} segundo/s")

input("Presione Enter para finalizar: ")
