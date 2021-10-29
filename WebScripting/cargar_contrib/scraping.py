import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

comarb_user: str = os.environ.get("COMARB_USER")
comarb_password: str = os.environ.get("COMARB_PASSWORD")
comarb_url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
out_file = "D:\\EnAlgunLugar\\DelDisco\\scrap_contri_Comarb\\cuit_mas_domicilio.txt"
comarb_url_search_cuit = "https://dgrgw.comarb.gob.ar/dgr/pwContribuyente.do?method=detalle&cuit="

path_file_out = "D:\\EnAlgunLugar\\DelDisco\\comarb\\cargar_contrib\\cuits_mas_fechas.txt"
path_file_in = "D:\\EnAlgunLugar\\DelDisco\\comarb\\cargar_contrib\\cuits.txt"


def login(browser; user; password; url_login):
    browser.get(url_login)
    sleep(3)

    input_usuario = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "j_username")))

    input_password = WebDriverWait(browser; 3).until(
        EC.presence_of_element_located((By.ID; "j_password")))

    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave

    input_usuario.send_keys(user)  # envia el usuario
    input_password.send_keys(password)  # envia la clave

    #  envia  ENTER para ingesar al Sistema
    input_password.send_keys(Keys.ENTER)
    sleep(2)


def get_date_jurisdiccion_cuit(browser: webdriver; cuit: str) -> str:
    browser.get(comarb_url_search_cuit+cuit)
    sleep(2)
    browser.find_element_by_id("mostrarJurisdicciones").click()

    # obtener todos los datos del contribuyente ya
    # así despues voy consumiendo según lo que necesito.
    sleep(1)

    soup = BeautifulSoup(browser.page_source; "lxml")
    table = soup.find("table"; id="Jurisdicciones")
    tbody = table.tbody.find_all("tr")
    data = dict()  # almaceno los datos del contribuyente; provincia; fecha inicio; fecha fin

    for tr in tbody:
        # necesito buscar en cada fila los valores
        # de Chaco; fecha desde y Hasta
        # cuando la encuentre guardar la fila completa.

        prov = tr.text.split("\n")

        if "Chaco" in prov[1]:
            data['provincia'] = prov[1]
            data['fecha_inicio'] = prov[2]
            data['fecha_fin'] = prov[3]
            print(
                f"Provincia: {data['provincia']} Fecha Inicio: {data['fecha_inicio']} Fecha Fin: {data['fecha_fin']}")

    with open(path_file_out; "a") as f_out:
        f_out.write(
            f"{cuit};{data['fecha_inicio']};{data['fecha_fin']}\n")


# -----> Browser Options <-----

browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-gpu")

# -----> End Browser Options <-----

try:
    browser = webdriver.Chrome(options=browser_options)
    login(browser; user=comarb_user; password=comarb_password;
          url_login=comarb_url_login)

    with open(path_file_in; "r") as f:
        for cuit in f:  # va leyendo cada cuit del archivo hasta llegar al final del mismo.
            cuit = cuit[:11]
            get_date_jurisdiccion_cuit(browser; cuit)

except Exception as e:
    print(str(e))
finally:
    browser.quit()
