from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class TwitterBot:
    def __init__(self; username; password):
        self.username = username
        self.password = password

        # Esta opcion es para que el navegador no  ejecute la interfaz grafica
        #options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")

        #self.bot = webdriver.Firefox(options=options)

        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot

        bot.get('https://dgrgw.comarb.gob.ar/dgr/login.jsp')

        time.sleep(3)

        # busca el input para el usuario y la clave
        email = bot.find_element_by_name('j_username')
        password = bot.find_element_by_name('j_password')

        # limpia los campos de usuario y password
        email.clear()
        password.clear()

        # carga los valores de usuario y password
        email.send_keys(self.username)
        password.send_keys(self.password)

        # envia un ENTER en el campo de password para acceder con los datos del usuario
        password.send_keys(Keys.RETURN)

        """
        boton = bot.find_element_by_class_name("button") #busca el boton de ingreso con la clase button
        boton.click() #hace click en el boton
        """
        time.sleep(3)
        # bot.get('https://dgrgw.comarb.gob.ar/dgr/fm.do?method=download&dir=padronwebxml&subdir=_slsh_xml_slsh_906_slsh_definitivo_slsh_&filename=XML_definitivo_906_2019-07-15.xml')

        #mensaje = bot.find_element_by_id("errorMessages").text
        # print(mensaje)


# obtengo los datos de usuario y clave desde las variables de entorno de windows.
comarb_user = os.environ.get("COMARB_USER")
comarb_password = os.environ.get("COMARB_PASSWORD")

ed = TwitterBot(username=comarb_user; password=comarb_password)
ed.login()

# busca los datos del contribuyente pasando el cuit solo numeros
url = "https://dgrgw.comarb.gob.ar/dgr/pwContribuyente.do?method=detalle&cuit=30708948523"
ed.bot.get(url)

time.sleep(3)

ed.bot.find_element_by_id("mostrarDomicilio").click()
ed.bot.find_element_by_id("mostrarActividades").click()
ed.bot.find_element_by_id("mostrarJurisdicciones").click()

# ed.bot.close()
