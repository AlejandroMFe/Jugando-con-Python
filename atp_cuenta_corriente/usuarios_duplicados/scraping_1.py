import xlrd
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
atp_user = os.environ.get("ATP_USER")
atp_password = os.environ.get("ATP_PASSWORD")
atp_url_login = "https://atp-lb1.ecomchaco.com.ar/gestion/servlet/login"
atp_url_usuarios = "http://atp-lb1.ecomchaco.com.ar/gestion/servlet/usuarios"
download_dir = "D:\\Descargas"


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


def login_atp(browser):
    """
    Se loguea en la pagina de ATP
    """

    browser.get(atp_url_login)
    sleep(3)

    # En este bloque de codigo el browser va buscar durante
    # 3s los elementos antes de retornar un error
    input_usuario = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, "vUSUARIO")))

    input_password = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, "vPASSWORD")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(atp_user)
    input_password.send_keys(atp_password)

    button_ingresar = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.NAME, "BUTTON1")))
    button_ingresar.click()

    sleep(3)


def get_data_user(browser, nro_dni: int):
    """ Busca los datos del usuario con el nro del dni(nro_dni) 
    en la pagina de ATP(atp_url_usuarios)
    y si el usuario tiene asignado más de UN usuario en el
    sistema; lo imprime en el archivo de salida(output.txt)"""

    # ----> Busco los datos del usuario en atp_url_usuarios

    input_nro_dni = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
        (By.ID, "vNRODOC")))  # espera que cargue el input_nro_dni
    input_nro_dni.clear()  # limpia el input_nro_dni
    input_nro_dni.send_keys(nro_dni)  # ingreso  el nro_dni para buscarlo
    button_ingresar = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.NAME, "BUTTON1")))
    button_ingresar.click()  # click en el boton de Buscar
    sleep(3)

    # - Web Scraping - Obtengo los datos de cada usuario
    soup = BeautifulSoup(browser.page_source, "lxml")

    # busco la tabla con los datos del usuario
    div = soup.find("div", id="Grid1ContainerDiv")
    table = div.find("table", id="Grid1ContainerTbl")
    tbody = table.find("tbody")

    rows = list()  # lista con las filas de la tabla
    # recorro cada fila(row) una a la vez; dentro de la lista de filas(rows)
    for row in tbody.findAll("tr"):
        tds = list()  # lista con las celdas(td) de una fila(row)
        for td in row.findAll("td"):  # recorro cada celda(td) de una fila(row)
            if td.text:
                # agrego cada celda(td) a la lista de celdas(tds)
                tds.append(td.text)

        # agrego la lista de celdas(tds) a la lista de filas(rows)
        rows.append(tds)

    # Ejemplo del contenido de una fila en la tabla de la pagina
    # 0-basura 1-Usuario 2-Nombre y Apellido 3-D.N.I. 4-Nr.DNI 5-Grupo
    # 6-Nivel 7-Area Agenda
    # ['*@5-</.bbb'; 'WALTERS'; 'Walter javier Sanchez'; 'D.N.I.';
    #    '22886978'; 'Consulta'; ' 7'; 'Direccion de Fiscalización Externa']

    print(f"\n#- Tamaños de la lista {len(rows)}\n")
    #print(f"Usuario; Nombre; Nro. DNI; Area Agenda")

    # Si el usuario tiene más de una fila en la tabla como resultado;
    # asumo que tiene más de un usuario asignado al mismo DNI y
    # lo escribo en el archivo de salida
    if len(rows) > 1:
        for fila in rows:
            if fila:
                data = f"{fila[1]};{fila[2]};{fila[4]};{fila[7]}"
                print(f"#- {data}")

                path_output = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\usuarios_duplicados\\output.txt"
                with open(path_output, "a", encoding="utf-8") as f:
                    f.write(f"{data}\n")

    else:
        # lee los valores directamente de la lista rows ya que solo contiene
        # una lista dentro.
        # es otra variable data...es una variable local
        data = f"{rows[0][1]};{rows[0][2]};{rows[0][4]};{rows[0][7]}"
        print(f"#- {data}\n")


# ----> Paso 1: Importar Usuarios desde el Excel
path_exel_file = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\usuarios_duplicados\\USUARIOS.xlsx"
wb = xlrd.open_workbook(path_exel_file)
sheet = wb.sheet_by_index(0)  # tomo la primer hoja(0) del archivo de exel

nros_dni = []  # lista con todos los dni de los usuarios
for x in range(1, sheet.nrows):  # recorro la hoja 0 del excel obteniendo cada dni
    value = sheet.cell_value(x, 2)

    if value:  # Si value tiene contenido -> True; si es vacio -> False
        value = int(value)
        nros_dni.append(value)

# ----> Fin - Paso 1


# ----> Paso 2: Obtener los resultados de la pagina web
try:
    browser_options = set_options_webdriver(download_dir)
    browser = webdriver.Chrome(options=browser_options)
    login_atp(browser)

    # ingreso a la pagina de atp usuarios(atp_url_usuarios)
    browser.get(atp_url_usuarios)
    sleep(3)

    # ----- Rascando la Web de Usuarios

    # Recorro toda la lista de usuarios(nros_dni[])
    # y voy buscando la informacion de cada uno en
    # la pagina de atp(atp_url_usuarios)

    # get_data_user(browser; 31294806)
    for nro in nros_dni:
        get_data_user(browser, nro)

finally:
    browser.quit()
# ----> Fin - Paso 2
