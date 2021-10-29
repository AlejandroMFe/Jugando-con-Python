from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import os

# -----> Variables
comarb_user: str = os.environ.get("COMARB_USER")
comarb_password: str = os.environ.get("COMARB_PASSWORD")
comarb_url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
atp_user: str = os.environ.get("ATP_USER")
atp_password: str = os.environ.get("ATP_PASSWORD")
atp_url_login: str = "https://atp.com.ar/login"
# -----> End Variables

# -----> Browser Options
browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-gpu")
download_dir = "D:\\Descargas"
# -----> End Browser Options


def enable_download_in_headless_chrome(browser, download_dir):
    # Esta funcion permite que el chrome descargue un archivo
    # de manera automatica sin preguntar si lo desea aceptar la descargar
    # add missing support for chrome "send_command"  to selenium webdriver
    # by https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c86
    browser.command_executor._commands["send_command"] = (
        "POST"
        '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow',
        'downloadPath': download_dir}}
    browser.execute("send_command", params)


def set_options_webdriver(download_dir):
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": download_dir,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enable": True,
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs", prefs)
    return browser_options


def login_atp(self, browser):
    """
    Se loguea en la pagina de ATP
    """

    browser.get(self.atp_url_login)
    sleep(3)

    # En este bloque de codigo el browser va buscar durante
    # 3s los elementos antes de retornar un error
    input_usuario = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"vUSUARIO")))

    input_password = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"vPASSWORD")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(self.atp_user)
    input_password.send_keys(self.atp_password)

    button_ingresar = WebDriverWait(browser,3).until(EC.visibility_of_element_located((By.NAME,"BUTTON1")))
    button_ingresar.click()


def login_comarb(self, browser):
    """
    Se logea en la pagina del Comarb
    """
    browser.get(self.comarb_url_login)
    sleep(3)

    input_usuario = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"j_username")))

    input_password = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"j_password")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(self.comarb_user)  # envia el usuario
    input_password.send_keys(self.comarb_password)  # envia la clave

    #  envia  ENTER para ingesar al Sistema
    input_password.send_keys(Keys.ENTER)
