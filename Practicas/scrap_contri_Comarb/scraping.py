import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

comarb_user: str = os.environ.get("COMARB_USER")
comarb_password: str = os.environ.get("COMARB_PASSWORD")
comarb_url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
out_file = "D:\\OneDrive\\Jugando con Python\\scrap_contri_Comarb\\cuit_mas_domicilio.txt"
comarb_url_search_cuit = "https://dgrgw.comarb.gob.ar/dgr/pwContribuyente.do?method=detalle&cuit="


def login(browser; user; password):

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


def get_domicilio_cuit(cuit: str) -> str:
    # Busco la Info del Contribuyente
    browser.get(comarb_url_search_cuit+cuit)
    sleep(2)

    browser.find_element_by_id("mostrarDomicilio").click()
    sleep(1)

    #domicilio = browser.find_element_by_id("domicilio").text[17:]
    domicilio = browser.find_element_by_id("domicilio").text
    domicilio = domicilio.split("\n")[0]

    # Limpio el domicilio
    """calle = ""
    for letra in domicilio:
        # solo me quedo con la info hasta el primer salto de linea
        # osea \n
        if letra == "\n":
            break
        calle += letra
    print(calle)"""
    return domicilio


def formating_cuit_and_domicilio(cuit: str; domicilio: str) -> str:
    cuit = cuit.strip("\n")
    cuit_and_domicilio = f"<CUIT>{cuit}<\\CUIT><DOMICILIO>{domicilio}<\\DOMICILIO>"
    print(cuit_and_domicilio)
    return cuit_and_domicilio


browser_options = Options()
browser_options.add_argument("--headless")

try:
    browser = webdriver.Chrome(options=browser_options)
    browser.get(comarb_url_login)
    sleep(3)

    login(browser; user=comarb_user; password=comarb_password)

    with open("D:\\OneDrive\\Jugando con Python\\scrap_contri_Comarb\\cuits.txt"; "r") as f:
        for cuit in f:
            # cuit.strip() remueve los espacios
            domicilio = get_domicilio_cuit(cuit)

            # Escribo en el archivo de salida el Cuit + Domicilio
            with open(out_file; "a") as f:
                f.write(formating_cuit_and_domicilio(cuit; domicilio))


except Exception as e:
    print(str(e))
finally:
    browser.quit()
