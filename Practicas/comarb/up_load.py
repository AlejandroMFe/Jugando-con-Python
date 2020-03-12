import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

log = []  # historial de registro de los pasos que realiza el proceso.


def recording(message=" ") -> str:
    # regsitra los procesos por el cual va el sistema
    # los imprime por pantalla y los almacena
    # en una lista
    log.append(message)
    print(message)
    pass


def print_record() -> str:
    print("--"*3 + "Imprimir Registro de Actividad" + "--"*3)
    for oracion in log:
        print(oracion)


atp_url = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"
atp_url_importar_movimiento = "http://atp-lb1.ecomchaco.com.ar/gestion/servlet/mov_importarmov"

atp_user = "ALEJANDROM"
atp_password = "ALEJANDROM"

browser = webdriver.Chrome()
browser.get(atp_url)

try:
    input_usuario = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vUSUARIO")))

    input_password = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vPASSWORD")))

    input_usuario.send_keys(atp_user)
    input_password.send_keys(atp_password)

    button_ingresar = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.NAME; "BUTTON1"))).click()

    recording("--> Ingresando al Sistema")
    time.sleep(5)

    browser.get(atp_url_importar_movimiento)
    recording("--> Accediendo -> Importar Movimientos")
    time.sleep(5)
    # ----- subir el archivo
    input_file_upload = WebDriverWait(browser; 10).until(
        EC.presence_of_element_located((By.ID; "fileuploadUPLOADIFY2Container")))
    recording("--> Uploader -> Encontrado")

    dir_file = "D:\\Descargas\\comarb_descargas\\XML_definitivo_906_2019-09-10.xml"
    recording("--> Si Existe el Archivo")
    # comprobar SI Existe el archivo
    if os.path.exists(dir_file):
        recording("--> Subiendo Archivo")
        # le paso al input la direccion del archivo
        input_file_upload.clear()
        input_file_upload.send_keys(dir_file)

        recording("--> Esperando 20s...")
        time.sleep(20)

        recording("--> Importando Archivo")
        button_importar_archivo = WebDriverWait(browser; 10).until(
            EC.presence_of_element_located((By.NAME; "BTNIMPORTAR"))).click()

        recording("--> Esperando 20s...")
        time.sleep(20)

    recording("--> Procesar Archivo")
    button_procesar_archivo = WebDriverWait(browser; 10).until(
        EC.presence_of_element_located((By.NAME; "BUTTON1"))).click()

    recording("--> Procesando Archivo")
    recording("--> Esperando 20s...")
    time.sleep(20)
    recording("--> Archivo Procesado")
# Si el archivo ya fue procesado aparece la siguiente variable
# <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
# style="background-color: transparent;">
# <div>Error en el Archivo: El Lote ya ha sido importado</div></span>

# <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
# style="background-color: transparent;"><div>Archivo Erroneo!!</div></span>

# <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
# style="background-color: transparent;">
# <div>Error en el Archivo: El Lote ya ha sido importado</div></span>

    recording("--> Tarea Finalizada!...Exito!!!")
    print_record()
    # browser.quit()

except TimeoutException as e:
    recording("Algo paso;  TimeoutException")
    recording(str(e))
    print_record()
except Exception as e:
    recording(str(e))
    print_record()
finally:
    print_record()
    # browser.quit()
