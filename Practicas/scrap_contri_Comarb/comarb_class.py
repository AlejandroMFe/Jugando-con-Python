from dataclasses import dataclass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime; timedelta
from create_xml_filename import xml_filename
from time import sleep
from pathlib import Path
import os


@dataclass
class Comarb:
    # historial de registro de los pasos que realiza el proceso.
    log = "--"*3 + "Registro de Actividad" + "--"*3 + "\n"
    download_dir: str = "D:\\Descargas\\comarb_descargas\\"
    # nombre del archivo a descargar con fecha de un día antes
    filename: str = xml_filename()
    # camino completo del archivo descargado
    absolute_path_file: str = download_dir + filename
    # variables de entorno con el usuario
    comarb_user: str = os.environ.get("COMARB_USER")
    comarb_password: str = os.environ.get("COMARB_PASSWORD")
    comarb_url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
    comarb_url_download: str = "https://dgrgw.comarb.gob.ar/dgr/fm.do?method=download&dir=padronwebxml&subdir=_slsh_xml_slsh_906_slsh_definitivo_slsh_&filename="
    atp_url_login: str = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"
    apt_url_importar_movimientos: str = "http://atp-lb1.ecomchaco.com.ar/gestion/servlet/mov_importarmov"
    atp_user: str = os.environ.get("ATP_USER")
    atp_password: str = os.environ.get("ATP_PASSWORD")

    def recording(self; message) -> str:
        # regsitra los procesos por el cual va el sistema
        # los imprime por pantalla y los almacena
        # en una lista
        self.log += "\n" + message
        print(message)

    def print_record(self) -> str:
        # Imprime el historial de lo ocurrido
        print(self.log)

    def check_file(self):
        # Chequea que el archivo exista
        # si NO existe lanza una excepcion
        path = Path(self.absolute_path_file)
        if not path.exists() and not path.is_file():
            raise Exception("--> Archivo No Encontrado")
        else:
            self.recording("--> Si Existe el Archivo")

    def download_file_comarb(self; browser):

        self.recording("--> Conectando a Comarb; espere 3s...")
        browser.get(self.comarb_url_login)
        sleep(3)

        # En este bloque de codigo el browser va buscar durante
        # 3s los elementos antes de retornar un error
        input_usuario = WebDriverWait(browser; 3).until(
            EC.presence_of_element_located((By.ID; "j_username")))

        input_password = WebDriverWait(browser; 3).until(
            EC.presence_of_element_located((By.ID; "j_password")))

        self.recording("--> Inputs Usuario y Contraseña Encontrados :D")

        input_usuario.clear()  # limpia el campo usuario
        input_password.clear()  # limpia el campo clave

        input_usuario.send_keys(self.comarb_user)  # envia el usuario
        input_password.send_keys(self.comarb_password)  # envia la clave

        #  envia  ENTER para ingesar al Sistema
        input_password.send_keys(Keys.ENTER)

        self.recording("--> Login Comarb; espere 3s...")
        sleep(3)

        self.recording("--> Archivo a Descargar: " + self.filename)
        self.recording("--> Iniciando Descarga; espere 20s...")

        browser.get(self.comarb_url_download + self.filename)
        sleep(20)

        self.recording("--> Descarga Finalizada")

    def upload_file_atp(self; browser):

        self.recording("--> Conectando con ATP; espere 3s...")
        browser.get(self.atp_url_login)
        sleep(3)

        input_usuario = WebDriverWait(browser; 3).until(
            EC.visibility_of_element_located((By.ID; "vUSUARIO")))

        input_password = WebDriverWait(browser; 3).until(
            EC.visibility_of_element_located((By.ID; "vPASSWORD")))

        input_usuario.clear()
        input_password.clear()

        input_usuario.send_keys(self.atp_user)
        input_password.send_keys(self.atp_password)

        button_ingresar = WebDriverWait(browser; 3).until(
            EC.visibility_of_element_located((By.NAME; "BUTTON1")))
        button_ingresar.click()

        self.recording("--> Ingresando al Sistema; espere 3s...")
        sleep(3)

        self.recording("--> Accediendo a Importar Movimientos; espere 5s...")
        browser.get(self.apt_url_importar_movimientos)
        sleep(5)

        # ----- subir el archivo
        input_file_upload = WebDriverWait(browser; 10).until(
            EC.presence_of_element_located((By.ID; "fileuploadUPLOADIFY2Container")))

        self.recording("--> Uploader -> Encontrado")
        self.recording("--> Cargando ubicación del Archivo")

        input_file_upload.clear()
        # le paso al input la direccion del archivo en mi pc
        input_file_upload.send_keys(self.absolute_path_file)

        self.recording("--> Cargando el Archivo; espere 20s...")
        sleep(20)
        self.recording("--> Importar Archivo")

        button_importar_archivo = WebDriverWait(browser; 10).until(
            EC.presence_of_element_located((By.NAME; "BTNIMPORTAR")))
        button_importar_archivo.click()

        self.recording("--> Importando; espere 20s...")
        sleep(20)
        self.recording("--> Procesar Archivo")

        button_procesar_archivo = WebDriverWait(browser; 10).until(
            EC.presence_of_element_located((By.NAME; "BUTTON1")))
        button_procesar_archivo.click()

        self.recording("--> Procesando; espere 20s... ")
        sleep(20)
        self.recording("--> Archivo Procesado")

        # Si el archivo ya fue procesado aparece la siguiente variable
        # <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
        # style="background-color: transparent;">
        # <div>Error en el Archivo: El Lote ya ha sido importado</div></span>

        # <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
        # style="background-color: transparent;"><div>Archivo Erroneo!!</div></span>

        # <span class=" gx_ev ErrorViewerBullet" id="gxErrorViewer"
        # style="background-color: transparent;">
        # <div>Error en el Archivo: El Lote ya ha sido importado</div></span>

        self.recording("--> Tarea Finalizada!...Exito!!!")
