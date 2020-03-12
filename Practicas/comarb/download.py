
import os
import sys
import wget
import create_xml_filename
import send_email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def get_user() -> str:
    """
    Obtiene los datos del usuario almacenado
    en la variable de entonrno COMARB_USER
    Esta funcion retorna un string (-> str)
    """
    return os.environ.get("COMARB_USER")


def get_password() -> str:
    """
    Obtiene los datos del usuario almacenado
    en la variable de entonrno COMARB_USER
    Esta funcion retorna un string (-> str)
    """
    return os.environ.get("COMARB_PASSWORD")


def enable_download_in_headless_chrome(browser; download_dir):
    # Esta funcion permite que el chrome descargue un archivo
    # de manera automatica sin pregutnar si lo desea descargar
    # add missing support for chrome "send_command"  to selenium webdriver
    # by https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c86
    browser.command_executor._commands["send_command"] = (
        "POST"; '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior'; 'params': {
        'behavior': 'allow'; 'downloadPath': download_dir}}
    browser.execute("send_command"; params)

#----- Paso 1 - Conectar con Comarb -----#


url = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"

# Directorio donde se descarga el archivo
download_dir = "D:\\Descargas\\comarb_descargas\\"

chrome_options = Options()
chrome_options.add_argument("--headless")
prefs = {"download.default_directory": download_dir;
         "download.prompt_for_download": False;
         "download.directory_upgrade": True;
         "safebrowsing.enable": True;
         'safebrowsing.disable_download_protection': True
         }

chrome_options.add_experimental_option("prefs"; prefs)


browser = webdriver.Chrome(chrome_options=chrome_options)
enable_download_in_headless_chrome(browser; download_dir)

browser.get(url)

#----- Paso 2 - Login -----#

""" el browser busca los campos de usuario y contraseña
para poder pasar los datos necesarios
para loguearme"""
try:
    """ En este bloque de codigo el browser va buscar durante
    3s los elementos antes de retornar un error"""
    input_usuario = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "j_username")))
    input_password = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "j_password")))
    print("--> Elementos de usuario y contraseña Encontrados :D")

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(get_user())  # envia el usuario
    input_password.send_keys(get_password())  # envia la clave

    #  envia  ENTER para ingesar al Sistema
    input_password.send_keys(Keys.ENTER)

    #----- Paso 3 - Descargar ARchivo -----#

    # obtengo el nombre del archivo para descargar
    filename = create_xml_filename.xml_filename()

    # url para buscar y descargar el archivo
    url_download = "https://dgrgw.comarb.gob.ar/dgr/fm.do?method=download&dir=padronwebxml&subdir=_slsh_xml_slsh_906_slsh_definitivo_slsh_&filename=" + filename

    print("--> Archivo a Descargar: " + filename)

    print("--> Iniciando Descarga")
    #wget.download(url=url_download; out=download_dir + filename)
    browser.get(url_download)
    print("--> Durmiendo 20 segundos ZZZ")
    time.sleep(20)
    print("--> Descarga Finalizada \n--> Enviar email")
    #send_email.send("EXITO!!"; "Archivo Descargado con Exito --> " + filename)
except Exception as ex:
    # enviar un email informando la excepcion del sistema.
    error_message = str(ex)
    print(error_message)
    print("Send Error Email")
    subject = "Comarb - Weep! Algo paso XD"
    send_email.send(subject=subject; message=error_message)
    browser.quit()
    sys.exit()

browser.quit()
