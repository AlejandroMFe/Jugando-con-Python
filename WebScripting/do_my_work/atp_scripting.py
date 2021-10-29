"""
Objetivo: obtener todos los contribuyentes que dieron error 
en el proceso de archivos de comarb.
"""

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
atp_url_login: str = "https://atp/login"
atp_url_archivos_importados: str = "http://atp/pw_archivosimp"
# -----> End Variables

# -----> Browser Options
browser_options = Options()
#browser_options.add_argument("--headless")
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



def login(browser):
    browser.get(atp_url_login)
    sleep(3)
    input_usuario = browser.find_element_by_xpath("//input[@id='vUSUARIO']")
    input_password = browser.find_element_by_xpath("//input[@id='vPASSWORD']")
    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave
    input_usuario.send_keys(atp_user)  # envia el usuario
    sleep(1) # necesita tiempo para escribir el usuario 
    input_password.send_keys(atp_password)  # envia la clave
    sleep(2) # necesita tiempo para escribir la clave
    # click en el boton "login" para ingresar al sistema
    browser.find_element_by_xpath("//input[@name='BUTTON1']").click()
    sleep(2)

try:
    browser = webdriver.Chrome(options=browser_options)
    login(browser)

    browser.get(atp_url_archivos_importados)
    sleep(3)
    soup = BeautifulSoup(browser.page_source, "lxml")
    
    # ---> Tabla Archivos Importados
    
    div = soup.find("div", id="Grid1ContainerDiv")
    table = div.find("table", id="Grid1ContainerTbl")
    tbody = table.find("tbody")

    # Esta lista(table_archivos_importados) contiene los datos de la tabla almacenados en un diccionario(td_data)
    table_archivos_importados = [] 
    for row in tbody.findAll("tr"):
        # td_data = {} es un diccionario con los datos de la tabla
        # Keys -> nombre de la columna
        # Values -> contenido de la columna
        td_data = {} 
        for td in row.findAll("td"): # 6 columnas
            # Cargo el diccionario td_data con los 
            # valores de cada celda por columna
            if td["colindex"] == "0": # tomo columna cuyo colindex = 0
                id_input = td.find("input")["id"] # del input quiero el valor de su id
                td_data["id_input"] = id_input
            elif td["colindex"] == "1":
                td_data["nro_lote"] = str(td.text).strip()
            elif td["colindex"] == "2":
                td_data["fecha_archivo"] = td.text
            elif td["colindex"] == "3":
                td_data["fecha_importacion"] = td.text
            elif td["colindex"] == "4":
                td_data["cant_registros"] = str(td.text).strip()
            elif td["colindex"] == "5":
                td_data["usuario"] = td.text
            else: # colindex == 6
                td_data["cant_errores"] = str(td.text).strip()
        #print(td_data)
        table_archivos_importados.append(td_data)
    #print(table_archivos_importados)
    
    # ---> FIN - Tabla Archivos Importados

    # Imprimo los id_input de los contribuyentes que tienen errores
    # para corregir
    list_with_errors = [contribuyente["id_input"] for contribuyente in table_archivos_importados if int(contribuyente["cant_errores"]) > 0]
    print("\n---> Lista de Errores: \n", list_with_errors)

    # click el icono de la hoja y lupa de la fila
    # que tiene errores.
    # fila con errores -> id en la list_with_errors
    sleep(2)
    #!TODO Recorrer todos las filas de la lista (list_with_errors) que tienen errores
    browser.find_element_by_xpath(f"//input[@name='{list_with_errors[0]}'][@id='{list_with_errors[0]}']").click()
    sleep(5)
    
    # Cambiar a la ventana emergente (Modal Windows in javascript)
    browser.switch_to.frame("gxp0_ifrm")
    # seleccionar la casilla de "Solo Trámites con Errores"
    browser.find_element_by_xpath("//input[@id='vERRORES']").click()
    sleep(2)

    # ---> Obetener datos Tabla de Transacciones, de la ventana emergente
    # Guardo los datos en un diccionario (trans_dic)
    # Cabecera de la Tabla
    #   Transacción Cuit Razón Social Trámite Estado Fecha Estado Act/Grab Cont. Resolver
    
    # trae el contenido de la tabla de la primer pagina
    tramites_errores = browser.find_element_by_xpath("//table[@id='Grid1ContainerTbl']//tbody").text
    
    
    
    # -> los datos estan todos escritos en UN solo Renglon
    # Necesito separarlos:
    # 1° Transformo la info en string para trabajar con ella
    text = str(tramites_errores)
    #print("\n---> TEXTO: \n", text)

    # 2° Creo una lista con cada linea en ella
    transacciones = [text[i:i+153]for i in range(0,len(text), 153)]
    #print("\n---> LISTA: \n", transacciones)
    
    
    # 3° Creo un diccionario con cada uno de los elementos
    # de la cabecera
    trans_dic = {}
    for tran in transacciones:
        trans_dic["transaccion"] = tran[:7]
        trans_dic["cuit"] = tran[8:21]
        trans_dic["razon_social"] = tran[22:56].strip()
        trans_dic["tramite"] = tran[56:107].strip()
        trans_dic["estado"] = tran[107:137].strip()
        trans_dic["fecha_estado"] = tran[137:].strip()
    
    print("\n---> DICCIONARIO: \n", trans_dic)
    # - hasta aca Funciona -

    


except Exception as identifier:
    pass
finally:
    browser.quit()