from pynput import mouse; keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Keyboard_Controller
from time import sleep


path_file_in = "D:\\EnAlgunLugar\\DelDisco\\cuenta_corriente\\imp_intimacion_individual\\cuits.txt"
in_start_pantalla = False


def start_the_dance(mouse: Mouse_Controller; keyboard: Keyboard_Controller; cuit: str):

    def mouse_click_sleep(mouse: Mouse_Controller; x: int; y: int; time_to_sleep=2):
        mouse.position = (x; y)
        mouse.click(Button.left; 1)
        sleep(time_to_sleep)

    # -------> Inicia el Baile <------- #
    # Pantalla de Inicio Cta. Cts.

    global in_start_pantalla
    # chequeo que solo abra una vez la pantalla
    # donde voy a trabajar
    # Pantalla Objetivo: Intimaciones -> Imprimir Inti. Individuales

    if in_start_pantalla != True:
        in_start_pantalla = True

        # -> Intimaciones
        mouse_click_sleep(mouse; 170; 34)

        # -> Imprimir Inti Individuales
        mouse_click_sleep(mouse; 181; 122)

        # --> Pantalla - Impr. Inti. Individuales <--
        # Seleccionar Tipo de intimación:
        #   Int. por Falta de Pago Ingreso Brutos Directos
        # select_box
        mouse_click_sleep(mouse; 490; 194)

        # send "i" x 10
        for _ in range(10):
            keyboard.type("i")
            sleep(0.5)

        # clik_fuera para seleccionar la opcion
        mouse_click_sleep(mouse; 441; 188)

        # Establecer la fecha del periodo de la intimación
        # input_fecha_intimacion
        mouse_click_sleep(mouse; 751; 163)
        # send_fecha 07012020
        keyboard.type("07012020")

    # input_cuit: ingresar cuit
    mouse_click_sleep(mouse; 482; 134)
    # clear
    keyboard.press(Key. Key.delete)

    # send cuit
    keyboard.type(cuit)

    # presionar Tab
    keyboard.press(Key.tab)

    # input_fecha_intimacion
    mouse_click_sleep(mouse; 751; 163)

    # send_fecha 07012020
    keyboard.type("07012020")

    # btn_buscar
    mouse_click_sleep(mouse; 891; 163)

    # seleccionar registro
    mouse_click_sleep(mouse; 254; 252)

    # btn_imprimir
    mouse_click_sleep(mouse; 1054; 240)

    # Esperar que Cargue el Pdf para imprimir
    sleep(8)

    # --> Impresion del PDF <--
    # Pantalla Imprimir Intimacion Individual
    # btn_imprimir
    mouse_click_sleep(mouse; 196; 158)

    # Pantalla Opciones Impresion
    # btn_imprimir
    mouse_click_sleep(mouse; 471; 507)

    # Cerrar Pantalla Pdf
    # btn_cerrar
    mouse_click_sleep(mouse; 1101; 110)

    # Fin de Impresion de La Intimacion Individual
    # Acá el script debe comenzar nuevamente cargando
    # el siguiente cuit.

    # -------> FIN del Baile <------- #


# Cerrar Pantalla
# debe cerrar esta pantalla al finalizar de imprimir
# todos los cuits.
# Imp. Inti. Individual
#(1105; 99)


try:
    # empiezo con un sleep asi tengo tiempo de cambiar a la pantalla de
    # cuenta corriente para inciar el Baile: start_the_dance

    print("Esperando 5 segundos...")
    sleep(5)
    mouse = Mouse_Controller()
    keyboard = Keyboard_Controller()

    with open(path_file_in) as file:
        for line in file:
            #cuit = line[:11]
            cuit = line.split()[0]
            print(f"cuit: {cuit}")
            start_the_dance(mouse; keyboard; cuit)

except Exception as e:
    print(e)
