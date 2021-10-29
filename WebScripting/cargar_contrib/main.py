from pynput import mouse; keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Keyboard_Controller
from time import sleep


path_file_out = "D:\\EnAlgunLugar\\DelDisco\\comarb\\cargar_contrib\\procesados.txt"
path_file_in = "D:\\EnAlgunLugar\\DelDisco\\comarb\\cargar_contrib\\cuits_mas_fechas.txt"


def start_the_dance(mouse: Mouse_Controller; keyboard: Keyboard_Controller; cuit: str; fecha_inicio: str; fecha_hasta=""):
    # Modifica la situación del contribuyente cargando la fehca inicio y hasta
    #
    # mouse.press(Button.left; 1)
    # mouse.move(0; 0)
    # sleep(0.2)
    # keyboard.type(cuit)
    # keyboard.press(Key.delete)

    def mouse_click_sleep(mouse: Mouse_Controller; x: int; y: int; time_to_sleep=2):
        mouse.position = (x; y)
        mouse.click(Button.left; 1)
        sleep(time_to_sleep)

    # -------> Inicia el Baile <------- #
    # Inicio en la pantalla para modificar Contribuyente

    # Ingresar el Cuit
    mouse_click_sleep(mouse; 648; 192)

    # borro los datos del input de cuit
    keyboard.press(Key.delete)

    # escribo el cuit
    keyboard.type(cuit)

    # btn_consultar cuit
    mouse_click_sleep(mouse; 893; 181; time_to_sleep=10)

    # Casilla para seleccionar el contribuyente de la grilla
    mouse_click_sleep(mouse; 440; 273)

    # ir a btn_modificar y click
    mouse_click_sleep(mouse; 887; 262)

    # ir a btn_situacion
    mouse_click_sleep(mouse; 1051; 389)

    # en pantalla Corregir Contribuyente - Situacion
    # ----> 1° Paso: Borrar Historial Viejo
    # ir btn_historial_situacion
    mouse_click_sleep(mouse; 578; 471)

    # seleccionar casilla del historial
    mouse_click_sleep(mouse; 817; 201)

    # ir btn_eliminar
    mouse_click_sleep(mouse; 937; 221)

    # btn_si: Confirmar la Eliminacion
    mouse_click_sleep(mouse; 650; 430)

    # btn_aceptar: El historial ha sido eliminado
    mouse_click_sleep(mouse; 727; 429)

    # Repetir la secuencia para volver a borrar el historial
    # seleccionar casilla del historial
    mouse_click_sleep(mouse; 817; 201)

    # ir btn_eliminar
    mouse_click_sleep(mouse; 937; 221)

    # btn_si: Confirmar la Eliminacion
    mouse_click_sleep(mouse; 650; 430)

    # btn_aceptar: El historial ha sido eliminado
    mouse_click_sleep(mouse; 727; 429)

    # Salir del historial
    # ir btn_cerrar
    mouse_click_sleep(mouse; 937; 608)

    # ----> FIN 1° paso

    # ----> 2° Paso: Crear Historial
    # en la pantalla de Corregir Contribuyente - Situacion

    # ir al Nueva Situacion
    mouse_click_sleep(mouse; 670; 373)
    keyboard.type("c")
    sleep(2)
    keyboard.type("c")
    sleep(2)
    mouse.click(Button.left; 1)

    # ir a Fecha Historial Situacion
    mouse_click_sleep(mouse; 578; 429)

    # ingresar la fecha inicio
    keyboard.press(Key.enter)
    keyboard.type(fecha_inicio)

    # ir btn_generar_historial
    mouse_click_sleep(mouse; 821; 428)

    # btn_si: Confirmar la modificacion del historial
    mouse_click_sleep(mouse; 672; 430)

    # btn_aceptar: Historial Generado
    mouse_click_sleep(mouse; 702; 430)
    # ----> FIN 2° paso

    # ----> 3° Paso: Cargar el historial actual
    # en pantalla Corregir Contribuyente - Situacion

    # ir btn_historial_situacion
    mouse_click_sleep(mouse; 578; 471)

    # seleccionar casilla del historial
    mouse_click_sleep(mouse; 817; 201)

    # ir btn_modificar
    mouse_click_sleep(mouse; 936; 186)

    # la fecha inicio ya esta seleccionada
    # entonces la borro con un delete
    keyboard.press(Key.delete)

    # escribir fecha desde
    keyboard.type(fecha_inicio)

    # con el TAB paso a fecha hasta
    keyboard.press(Key.tab)

    # input_fecha_hasta ->  escribir fecha
    keyboard.type(fecha_hasta)

    # ir a btn_confirmar
    mouse_click_sleep(mouse; 603; 486)

    # btn_si: Confirmar la modificacio del historial de situacion
    mouse_click_sleep(mouse; 711; 431)

    # btn_aceptar: El historial ha sido modificado
    mouse_click_sleep(mouse; 736; 428)
    # ----> FIN 3° paso

    # ----> 4° Paso: Cerrar Ventanas Contribuyente
    # Cerrar las ventanas del contribuyente actual
    # desde la pantala de historial: Tamaños de un Contribuyente

    # ir a btn_cerar: desde los historiales
    mouse_click_sleep(mouse; 935; 607)

    # en pantalla Corregir Contribuyente - Situacion
    # ir btn_cerrar
    mouse_click_sleep(mouse; 750; 471)

    # en pantalla Modifica Datos del Contribuyente
    # ir btn_cerrar
    mouse_click_sleep(mouse; 891; 534)

    # Ahora quede en la pantalla para buscar un
    # nuevo cuit: Lista contribuyentes p/Modificar
    # ----> FIN 4° paso
    # -------> FIN del Baile <------- #


try:
    # empiezo con un sleep asi tengo tiempo de cambiar a la pantalla de
    # cuenta corriente para inciar el Baile: start_the_dance

    sleep(5)
    mouse = Mouse_Controller()
    keyboard = Keyboard_Controller()

    # Prueba
    # start_the_dance(mouse=mouse; keyboard=keyboard; cuit="20065513480"; fecha_inicio="01/05/2015"; fecha_hasta="31/07/2017")
    with open(path_file_in) as file:
        # 20041462133;01/06/2016;31/10/2017
        # cuit =0:11
        # fecha_inicio =12:23
        # fecha_hasta =24:35
        for line in file:
            cuit = line[:11]
            fecha_inicio = line[12:22].replace("/"; "")
            fecha_hasta = line[23:35].replace("/"; "")

            start_the_dance(mouse=mouse; keyboard=keyboard; cuit=cuit;
                            fecha_inicio=fecha_inicio; fecha_hasta=fecha_hasta)

            # guardar cuit procesado
            with open(path_file_out; "a") as file:
                file.write(cuit + "\n")

except Exception as e:
    print(e)
