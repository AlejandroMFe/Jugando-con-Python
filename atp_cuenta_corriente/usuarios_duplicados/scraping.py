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


def set_options_webdriver():
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": download_dir,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enable": True,
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs",prefs)
    return browser_options


def login_atp(browser):
    """
    Se loguea en la pagina de ATP
    """

    browser.get(atp_url_login)
    sleep(3)

    # En este bloque de codigo el browser va buscar durante
    # 3s los elementos antes de retornar un error
    input_usuario = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"vUSUARIO")))

    input_password = WebDriverWait(browser,3).until(
        EC.presence_of_element_located((By.ID,"vPASSWORD")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(atp_user)
    input_password.send_keys(atp_password)

    button_ingresar = WebDriverWait(browser,3).until(
        EC.visibility_of_element_located((By.NAME,"BUTTON1")))
    button_ingresar.click()

    sleep(3)


def get_data_user(browser, user):
    """ Busca los datos del usuario(user) en la pagina de ATP(atp_url_usuarios)
    y si el usuario tiene asignado más de UN usuario en el
    sistema, lo imprime en el archivo de salida(output.txt)"""

    # ---- Busco los datos del usuario en atp_url_usuarios

    input_user = WebDriverWait(browser,5).until(EC.presence_of_element_located(
                                   (By.ID,"vUSUARIO")))  # espera que cargue el input_user
    input_user.clear()  # limpia el input_user
    input_user.send_keys(user)  # ingreso  el usuario para ser buscado
    input_user.send_keys(Keys.ENTER)  # busca el resultado
    sleep(3)

    # ---- Obtener los resultados de cada usuario
    # Tabla que Contiene los resultados del usuario
    # <table id="Grid1ContainerTbl"
    #    <tbody>
    #        <tr id="Grid1ContainerRow_0001"
    #            <td valign="middle" colindex="1" style="text-align:left,">
    #                <span class="ReadonlyAttribute" style=",height: 17px," id="span_USUDES_0001">YESICA</span></td>

    soup = BeautifulSoup(browser.page_source,"lxml")

    div = soup.find("div",id="Grid1ContainerDiv")
    table = div.find("table",id="Grid1ContainerTbl")
    tbody = table.find("tbody")  # cuerpo de la tabla
    rows = tbody.find_all("tr")  # busco todas las filas(rows) en (tbody)

    data_table_list = []  # lista de la lista de filas(rows) [[]]
    row_list = []  # lista compuesta por celdas(td) de cada fila(row)

    for row in rows:  # recorro fila(row) por fila

        # busco todas las celdas(tds) en una fila(row)
        tds = row.find_all("td")

        for td in tds:
            td = td.text.strip()  # tomo el texto de cada celda(td) y le quito los espacios

            # Si la celda(td) NO esta vacia, la Agrega a la lista
            if td:  # Si td(tiene contenido) retorna True
                # agrego el contenido de la celda(td) a la lista de filas(row_list)
                row_list.append(td)

        # agrego la lista de fila(row_list) a la lista de la tabla(data_table_list)
        data_table_list.append(row_list)

    # imprime cada dato(td) en la fila(row_list)
    # for data in row_list:
    #    print(data)
    # print(row_list)
    # imprime
    # ['(<.8>@bbbb', 'YESICA', 'Dusicka Yesica Daiana', 'D.N.I.', '36902790', 'Consulta', '5', 'Administracion General']
    # print()
    # print(data_table_list)
    # imprime
    # [['(<.8>@bbbb', 'YESICA', 'Dusicka Yesica Daiana', 'D.N.I.', '36902790', 'Consulta', '5', 'Administracion General']]

    # escribo en el archivo de salida(outpu.txt) el contenido de la lista de la tabla(data_table_list)
    with open("D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\usuarios_duplicados\\output.txt","a") as f:
        if len(data_table_list) > 1:
            f.write(f"# Usuario: {user}\n")
            print(f"# Usuario: {user}")
            # f.write(f"    {str(data_table_list)}\n")

            for _, data in enumerate(data_table_list):
                # print(str(data))
                # ['(<.8>@bbbb', 'YESICA', 'Dusicka Yesica Daiana', 'D.N.I.', '36902790', 'Consulta', '5', 'Administracion General']
                usuario = str(data[1])
                nombre = str(data[2])
                f.write(f"    {usuario} --> {nombre}\n")
                print(f"    {usuario} --> {nombre}")
                # YESICA --> Dusicka Yesica Daiana
        else:
            print(f"\n --> la Lista contiene UN elemento\n")


# ----> Paso 1: Importar Usuarios desde el Excel
path_exel_file = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\usuarios_duplicados\\USUARIOS.xlsx"
wb = xlrd.open_workbook(path_exel_file)
sheet = wb.sheet_by_index(0)  # tomo la primer hoja(0) del archivo de exel

users = []  # lista con todos los usuarios
for x in range(1,sheet.nrows):  # recorro la hoja 0 del excel obteniendo cada usuario
    value = sheet.cell_value(x, 0)
    value = str(value).strip()

    if value:
        users.append(value)

# ----> Fin - Paso 1


# ----> Paso 2: Obtener los resultados de la pagina web
try:
    browser_options = set_options_webdriver()
    browser = webdriver.Chrome(options=browser_options)
    login_atp(browser)

    # ingreso a la pagina de atp usuarios(atp_url_usuarios)
    browser.get(atp_url_usuarios)
    sleep(3)

    # ----- Rascando la Web de Usuarios

    # Recorro toda la lista de usuarios(users[])
    # y voy buscando la informacion de cada uno en
    # la pagina de atp(atp_url_usuarios)
    # get_data_user(browser, users[0])
    for user in users:
        get_data_user(browser,user)


finally:
    browser.quit()
# ----> Fin - Paso 2
