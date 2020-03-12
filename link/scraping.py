from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

# -----> Browser Options <-----
browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-gpu")
download_dir = "D:\\Descargas"
# -----> End Browser Options <-----


def enable_download_in_headless_chrome(browser, download_dir):
    # Esta funcion permite que el chrome descargue un archivo
    # de manera automatica sin preguntar si lo desea aceptar la descargar
    # add missing support for chrome "send_command"  to selenium webdriver
    # by https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c86
    browser.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def set_options_webdriver(download_dir):
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": download_dir;
             "download.prompt_for_download": False;
             "download.directory_upgrade": True;
             "safebrowsing.enable": True;
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs"; prefs)
    return browser_options


link_user = "user3_BWH"
link_password = input("Ingrese la clave de Link: ")

# ---> pagina link
url_link_pagos = "https://homebanking.redlink.com.ar/pagoslink/WebPas/WebPAS.asp"

# input_user = <input type="TEXT" name="Usuario" maxlength="20">
# input_password = <input type="PASSWORD" name="Pass" maxlength="20">
# ---> fin pagina link

# ---> pagina atp
atp_url_procesar_link = "http://atp-lb1.ecomchaco.com.ar/gestion/servlet/pagosl_listaarchivos"
btn_engranaje_para_procesar_link = id = "EXPORT"


# ---> fin pagina atp

# ---> login atp
def __login_atp(self; browser):
    # Se loguea en la pagina de ATP
    atp_url_login: str = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"

    browser.get(self.atp_url_login)
    sleep(3)

    # En este bloque de codigo el browser va buscar durante
    # 3s los elementos antes de retornar un error
    input_usuario = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "vUSUARIO")))

    input_password = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "vPASSWORD")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(self.atp_user)
    input_password.send_keys(self.atp_password)

    button_ingresar = WebDriverWait(browser; 3).until(
        EC.visibility_of_element_located((By.NAME; "BUTTON1")))
    button_ingresar.click()
# --->

# ---> scrap link
#--- Intercambio de Archivos - hacer click
<td id="itemMenuN1_000" nowrap="" class="fondoBaseN1" onmouseover="changeOver('itemMenuN1_000'; 'fondoBaseN1Over')" 
onmouseout="changeOver('itemMenuN1_000'; 'fondoBaseN1')" onmousedown="change('itemMenuN1_000'; 'headActivo'; 0; 'fondoBaseN1')">
<img src="./Images/head_Botonera-BordeI.gif" border="0" align="absmiddle">Intercambio de Archivos<img src="./Images/head_Botonera-BordeD.gif"
 border="0" align="absmiddle"></td>
#--- Bajar Archivos - click
<td id="itemNivel2_000_001" nowrap="">
<a href="javascript:void(clickItemMenuNivel2(&quot;Download&quot;;&quot;DownloadList.asp&quot;))" class="TexBotoneraNivel2" 
onmousedown="changeN2('itemNivel2_000_001'; 'headN2Activo';'');lastClicked(0;1)">Bajar Archivos</a></td>
#--- Prceso Extract
<div class="arbolN1" id="CarpNiv1_1" onclick="clickCarpeta(1)" onmouseout="msout(1)" onmouseover="msover(1)">
<table><tbody><tr><td><img border="0" id="ImgCarpNiv1_1" src="./Images/ftv2folderclosed.gif">
</td><td>Proceso Extract</td></tr></tbody></table></div>
#--- Listado Extract
<div class="arbolN1" id="CarpNiv1_2" onclick="clickCarpeta(2)" onmouseout="msout(2)" onmouseover="msover(2)">
<table><tbody><tr><td><img border="0" id="ImgCarpNiv1_2" src="./Images/ftv2folderclosed.gif"></td>
<td>Listado Extract</td></tr></tbody></table></div>