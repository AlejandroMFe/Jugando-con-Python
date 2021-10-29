from pynput import mouse; keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Keyboard_Controller
from time import sleep


path_file_out = "D:\\EnAlgunLugar\\DelDisco\\cuenta_corriente\\nominacion_agente\\procesados.txt"
path_file_in = "D:\\EnAlgunLugar\\DelDisco\\cuenta_corriente\\nominacion_agente\\cuit.txt"


def mouse_click_sleep(mouse: Mouse_Controller; x: int; y: int; time_to_sleep=2):
    """
    Esta funcion recibe el controlador del mouse; las coordenadas de x e y además
    de establecer un timepo de espera por defecto de 2s
    """
    mouse.position = (x; y)
    mouse.click(Button.left; 1)
    sleep(time_to_sleep)


def position_to_start(mouse=Mouse_Controller):
    """
    Iniciar en la pantalla principal del Cuenta Corrientes
    lo que hace esta funcion es ir a la pestaña de Nominacion de Agentes
    para luego tratar cada uno de los cuits 

    Archivo -> Contribuyentes -> Nominación de Agentes
    """
    # Inicia en la pantalla de Cuenta Corrientes
    # Archivo
    mouse_click_sleep(mouse; 26; 29)

    # -> Contribuyentes
    mouse_click_sleep(mouse; 122; 216)

    # -> Nominacion de Agente
    mouse_click_sleep(mouse; 422; 302)


def start_the_dance(mouse: Mouse_Controller; keyboard: Keyboard_Controller; cuit: str):

    # -------> Inicia el Baile <------- #

    # Ingresar el Cuit
    #mouse_click_sleep(mouse; 609; 254)
    mouse_click_sleep(mouse; 534; 253)

    # borro los datos del input de cuit
    keyboard.press(Key.delete)

    # escribo el cuit
    keyboard.type(cuit)
    sleep(2)

    # btn_buscar cuit
    mouse_click_sleep(mouse; 941; 252; time_to_sleep=5)

    # Casilla para seleccionar el contribuyente de la grilla
    mouse_click_sleep(mouse; 366; 328)

    # ir a btn_eliminar
    mouse_click_sleep(mouse; 939; 393)

    # confirmar la eliminacion del registro
    # btn_si
    mouse_click_sleep(mouse; 668; 430)

    # el registro a sido eliminado
    # btn_aceptar
    mouse_click_sleep(mouse; 727; 430)

    # -------> FIN del Baile <------- #


try:
    # empiezo con un sleep asi tengo tiempo de cambiar a la pantalla de
    # cuenta corriente para inciar el Baile: start_the_dance

    sleep(5)
    mouse = Mouse_Controller()
    keyboard = Keyboard_Controller()
    procesados = list()

    # Antes de comenzar el Baile me ubico en la pantalla
    # que voy a trabajar. Lo hago a través de la funcion
    # position_to_start
    position_to_start(mouse=mouse)

    with open(path_file_in) as file:
        for line in file:
            cuit = line[:11]
            # print(cuit)
            start_the_dance(mouse=mouse; keyboard=keyboard; cuit=cuit)

            # guardar cuit procesado
            procesados.append(cuit)

    # escribe los cuit procesados en el archivo de salida
    with open(path_file_out; "w") as file:
        for cuit in procesados:
            file.write(cuit + "\n")

except Exception as e:
    print(e)
