from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import os

url_login: str = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"
url_search_cuit = "https://dgrgw.comarb.gob.ar/dgr/pwContribuyente.do?method=detalle&cuit="
comarb_user: str = os.environ.get("COMARB_USER")
comarb_password: str = os.environ.get("COMARB_PASSWORD")


def login(browser):
    browser.get(url_login)
    sleep(3)
    input_usuario = browser.find_element_by_xpath("//input[@id='j_username']")
    input_password = browser.find_element_by_xpath("//input[@id='j_password']")
    input_usuario.clear()  # limpia el campo usuario
    input_password.clear()  # limpia el campo clave
    input_usuario.send_keys(comarb_user)  # envia el usuario
    sleep(1) # necesita tiempo para escribir el usuario 
    input_password.send_keys(comarb_password)  # envia la clave
    sleep(2) # necesita tiempo para escribir la clave
    # click en el boton "login" para ingresar al sistema
    browser.find_element_by_xpath("//input[@name='login']").click()
    sleep(2)


def display_info_contribuyente(browser: webdriver, cuit: str):
    browser.get(url_search_cuit+cuit)
    browser.find_element_by_xpath("//a[@id='mostrarDomicilio']").click()
    browser.find_element_by_xpath("//a[@id='mostrarActividades']").click()
    browser.find_element_by_xpath("//a[@id='mostrarJurisdicciones']").click()
    sleep(2)


# -----> Browser Options <-----
browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-gpu")
# -----> End Browser Options <-----


#cuit = "30631377307"
cuit= "20177092364"


try:
    browser = webdriver.Chrome(options=browser_options)
    login(browser)
    display_info_contribuyente(browser, cuit)
   
    soup = BeautifulSoup(browser.page_source, "lxml")
    
    # ---> Tabla - Datos del Contribuyente 
    # Obtengo los datos del contribuyente de la primer tabla de la web.
    table = soup.find("table") # tabla con datos del contribuyente
    tbody  = table.find("tbody")

    # Cargo un Diccionario(data_contrib) con todos los datos
    # del contribuyente
    data_contrib = {}
    for index, row in enumerate(tbody.findAll("tr")):
        if index ==0: # primer fila(row) con datos(td)
            for index,td in enumerate(row.findAll("td")):
                if index == 0:
                    data_contrib["cuit"] = str(td.text).strip()
                elif index == 1:
                    data_contrib["nro_inscripcion"] = str(td.text).strip()
                else: # index == 2
                    data_contrib["razon_social"] = str(td.text).strip()
        else: # index == 1 segunda fila(row) con datos(td)
            for index,td in enumerate(row.findAll("td")):
                if index == 0:
                    data_contrib["contrib_sicom"] = str(td.text).strip()
                else: # index == 1
                    data_contrib["jurisdiccion_sede"] = str(td.text).strip()

    # ---> FIN - Datos del Contribuyente

    # ---> Tabla - Domicilios del Contribuyente
    div = soup.find("div",id="domicilio")
    table = div.find("table")
    tbody = table.find("tbody")

    domicilios = {}
    for index, row in enumerate(tbody.findAll("tr")):
        if index ==0: # 1 fila Domicilio Fiscal(row) con datos(td)
            td = row.find("td") 
            domicilios["domicilio_fiscal"] = str(td.text).strip()
        elif index == 1: # 2 fila Domicilio Principal de Actividades
            td = row.find("td")
            domicilios["domicilio_principal"] = str(td.text).strip()
        else: # 3 fila Naturaleza Juridica
            td = row.find("td")
            domicilios["naturaleza_juridica"] = str(td.text).replace("\n", "").strip()
    
    print(f"#   Domicilios:\n\t{domicilios}\n")
    # ---> FIN - Domicilios del Contribuyente
    

    # ---> Tabla - Actividades

    div = soup.find("div", id="actividades")
    table = div.find("table", id="Actividades")
    tbody = table.find("tbody")

    # data_rows es una lista que contiene otras listas con 
    # cada fila de informacion sobre 
    # las actividades del contribuyente
    #
    # Nomenclador -Cod Activ-Actividad-Art- Tipo-Fecha Alta-Fecha Baja
    #       0           1       2       3     4       5          6  
    
    actividades =[] # lista [con lista[td]]
    for row in tbody.findAll("tr"):
        data_tds = [td.text for td in row.findAll("td")]
        actividades.append(data_tds)
        # Resultado - Ejemplo:
        # [
        #   ['CUACM', '930990', 'Servicios personales n.c.p.', '002', 'S','01/04/1993', '31/12/2017'],
        #   ['NAES', '960990', 'Servicios personales n.c.p.', '002', 'P', '01/04/1993', '']
        # ]
            
    #print(actividades)
    # for data in actividades:
    #     if data[0] == "NAES":
    #         print(data)
    
    # ---> FIN - Actividades

    # ---> Tabla - Jurisdicciones
    
    div  = soup.find("div", id="jurisdicciones")
    table = div.find("table", id="Jurisdicciones")
    tbody = table.find("tbody")

    jurisdicciones = [] # lista[[]] con los datos de la tabla de jurisdicciones
    for row in tbody.findAll("tr"):
        data_tds = [td.text for td in row.findAll("td")]
        jurisdicciones.append(data_tds)
    # Resultado - Ejemplo:
    # [
    #   ['901 - Capital Federal', '01/12/2017', '30/04/2018'],
    #   ['902 - Buenos Aires', '01/12/2017', ''],
    #   ['906 - Chaco', '01/12/2017', ''],
    #   ['910 - Jujuy', '01/02/2018', '30/01/2020']
    # ] 

    print(jurisdicciones)
    if  jurisdicciones[2] != "":  
        print("Contribuyente Activo en Chaco")
        
    # ---> FIN - Jurisdicciones

except Exception as identifier:
    pass

finally:
    browser.quit()