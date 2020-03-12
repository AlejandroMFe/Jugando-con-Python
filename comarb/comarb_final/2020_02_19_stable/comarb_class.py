from dataclasses import dataclass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
from bs4 import BeautifulSoup
import os


@dataclass
class Comarb:
    # historial de registro de los pasos que realiza el proceso.
    log = "--"*3 + "Registro de Actividad" + "--"*3 + "\n"
    download_dir: str = "D:\\Descargas\\comarb_descargas\\"
    # nombre del archivo a descargar con fecha de un día antes
    xml_filename: str = ""
    # camino completo del archivo descargado
    absolute_path_file: str = ""
    # variables de entorno con el usuario
    comarb_user: str = os.environ.get("COMARB_USER")
    comarb_password: str = os.environ.get("COMARB_PASSWORD")
    comarb_url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
    comarb_url_download: str = "https://dgrgw.comarb.gob.ar/dgr/fm.do?method=download&dir=padronwebxml&subdir=_slsh_xml_slsh_906_slsh_definitivo_slsh_&filename="
    atp_url_login: str = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"
    apt_url_importar_movimientos: str = "http://atp-lb1.ecomchaco.com.ar/gestion/servlet/mov_importarmov"
    atp_url_archivos_importados: str = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/pw_archivosimp"
    atp_user: str = os.environ.get("ATP_USER")
    atp_password: str = os.environ.get("ATP_PASSWORD")

    def recording(self, message) -> str:
        # regsitra los procesos por el cual va el sistema
        # los imprime por pantalla y los almacena
        # en una lista
        self.log += "\n" + message
        print(message)

    def print_record(self) -> str:
        # Imprime el historial de lo ocurrido
        print(self.log)

    def __check_file_existence(self):
        # Chequea que el archivo exista
        # si NO existe lanza una excepcion
        
        # Cuando aún esta descargando el archivo el chrome los nombra
        # como: XML_definitivo_906_2020-02-17.xml.crdownload
        chrome_download_extension = ".crdownload"
        file_steel_download = self.absolute_path_file + chrome_download_extension
        path_file_steel_download = Path(file_steel_download)
        
        while path_file_steel_download.exists():
            sleep(1)
            print("Descargando...")

        path = Path(self.absolute_path_file)
        if path.exists() and path.is_file():
            self.recording("--> Archivo Si Existe")
        
        else:
            raise Exception("--> Archivo No Encontrado")

    def __login(self, browser, option):
        # Se loguea en la pagina que coresponda segun la opcion
        # option puede ser "atp" o "comarb"
        self.recording("--> Ingresando a {}, espere 3s...".format(option))

        if option == "atp":
            browser.get(self.atp_url_login)
            sleep(3)

            # En este bloque de codigo el browser va buscar durante
            # 3s los elementos antes de retornar un error
            input_usuario = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.ID, "vUSUARIO")))

            input_password = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.ID, "vPASSWORD")))

            input_usuario.clear()  # limpia el campo usuario
            input_password.clear()  # limpia el campo clave

            input_usuario.send_keys(self.atp_user)
            input_password.send_keys(self.atp_password)

            button_ingresar = WebDriverWait(browser, 3).until(
                EC.visibility_of_element_located((By.NAME, "BUTTON1")))
            button_ingresar.click()

        elif option == "comarb":
            browser.get(self.comarb_url_login)
            sleep(3)

            input_usuario = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.ID, "j_username")))

            input_password = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.ID, "j_password")))

            input_usuario.clear()  # limpia el campo usuario
            input_password.clear()  # limpia el campo clave

            input_usuario.send_keys(self.comarb_user)  # envia el usuario
            input_password.send_keys(self.comarb_password)  # envia la clave

            #  envia  ENTER para ingesar al Sistema
            input_password.send_keys(Keys.ENTER)

        self.recording("--> Ingresando al Sistema, espere 3s...")
        sleep(3)

    def set_xml_filename(self, date: str):
        # date -> YYYY-mm-dd
        # Crea el nombre del archivo xml a descargar
        year = date[:4]
        month = date[5:7]
        day = date[8:]

        # Retorna el nombre completo del archivo como un string
        self.xml_filename = "XML_definitivo_906_{0}-{1}-{2}.xml".format(
            year, month, day)
        self.absolute_path_file = self.download_dir + self.xml_filename

    def get_date_last_file_processed(self, browser) -> str:
        # Busco la fecha del ultimo archivo que fue procesado
        # en la pagina de ATP en archivos importados
        self.__login(browser, "atp")
        browser.get(self.atp_url_archivos_importados)
        sleep(3)

        # Obtengo la fecha  del ultimo archivo procesado
        soup = BeautifulSoup(browser.page_source, "lxml")
        table = soup.find("table", id="Grid1ContainerTbl")
        date_last_file_processed = table.tbody.tr.find(
            id="span_PADWEBFARC_0001").text

        # date_last_file_processed = table.tbody.find(
        #    "tr", id="Grid1ContainerRow_0006").find("td", colindex="2").text

        self.recording(
            "--> Ultimo Archio procesado en ATP: {}".format(date_last_file_processed))

        return date_last_file_processed

    def download_file_comarb(self, browser):

        self.__login(browser, "comarb")

        self.recording("--> Archivo a Descargar: " + self.xml_filename)
        self.recording("--> Iniciando Descarga, espere 20s...")

        browser.get(self.comarb_url_download + self.xml_filename)
        sleep(20)

        self.recording("--> Descarga Finalizada")

    def upload_file_atp(self, browser):

        self.__check_file_existence()
        self.__login(browser, "atp")

        self.recording("--> Accediendo a Importar Movimientos, espere 5s...")
        browser.get(self.apt_url_importar_movimientos)
        sleep(5)

        # ----- subir el archivo
        input_file_upload = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fileuploadUPLOADIFY2Container")))

        self.recording("--> Uploader -> Encontrado")
        self.recording("--> Cargando ubicación del Archivo")

        input_file_upload.clear()
        # le paso al input la direccion del archivo en mi pc
        input_file_upload.send_keys(self.absolute_path_file)

        self.recording("--> Cargando el Archivo, espere 20s...")
        sleep(20)
        self.recording("--> Importar Archivo")

        button_importar_archivo = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "BTNIMPORTAR")))
        button_importar_archivo.click()

        self.recording("--> Importando, espere 20s...")
        sleep(20)
        self.recording("--> Procesar Archivo")

        button_procesar_archivo = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "BUTTON1")))
        button_procesar_archivo.click()

        self.recording("--> Procesando, espere 20s... ")
        sleep(20)
        self.recording("--> Archivo Procesado")
        self.recording("--> Tarea Finalizada!...Exito!!!")
