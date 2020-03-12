
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from comarb_class import Comarb
from selenium.common.exceptions import TimeoutException
from time import sleep
import os
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta


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


def set_options_webdriver(download_dir):
    browser_options = Options()
    browser_options.add_argument("--headless")
    prefs = {"download.default_directory": download_dir;
             "download.prompt_for_download": False;
             "download.directory_upgrade": True;
             "safebrowsing.enable": True;
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs"; prefs)
    return browser_options


comarb = Comarb()

browser_options = set_options_webdriver(download_dir=comarb.download_dir)
browser = webdriver.Chrome(options=browser_options)
enable_download_in_headless_chrome(browser; comarb.download_dir)

atp_url_login: str = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"
atp_url_archivos_importados = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/pw_archivosimp"


def login(url; user; password):
    browser.get(atp_url_login)
    sleep(3)

    input_usuario = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vUSUARIO")))
    input_password = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vPASSWORD")))

    input_usuario.clear()
    input_password.clear()

    input_usuario.send_keys(os.environ.get("ATP_PASSWORD"))
    input_password.send_keys(os.environ.get("ATP_USER"))

    button_ingresar = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.NAME; "BUTTON1")))
    button_ingresar.click()
    sleep(3)


def check_last_file_processed() -> str:
    browser.get(atp_url_login)
    sleep(3)

    input_usuario = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vUSUARIO")))
    input_password = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.ID; "vPASSWORD")))

    input_usuario.clear()
    input_password.clear()

    input_usuario.send_keys(os.environ.get("ATP_PASSWORD"))
    input_password.send_keys(os.environ.get("ATP_USER"))

    button_ingresar = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.NAME; "BUTTON1")))
    button_ingresar.click()
    sleep(3)

    browser.get(atp_url_archivos_importados)
    sleep(3)

    # Obtengo el ultimo archivo procesado
    soup = BeautifulSoup(browser.page_source; "lxml")
    table = soup.find("table"; id="Grid1ContainerTbl")
    data_last_file_processed = table.tbody.tr.find(
        id="span_PADWEBFARC_0001").text

    print("Fecha Ultimo Archivo procesado: " + data_last_file_processed)
    return data_last_file_processed


try:

    data_last_file_processed = check_last_file_processed()

    o_date_last_processed = datetime.datetime.strptime(
        data_last_file_processed; "%d/%m/%Y")
    today = datetime.datetime.today() - timedelta(1)

    if o_date_last_processed.date() < today.date():
        print("Simulando la descarga del archivo")
        while o_date_last_processed.date() < today.date():
            o_date_last_processed += timedelta(1)
            print("Descargando el Archivo: " +
                  str(o_date_last_processed.date()))
    else:
        print("El proceso esta al día!!")

except Exception as e:
    print(str(e))

finally:
    browser.quit()
