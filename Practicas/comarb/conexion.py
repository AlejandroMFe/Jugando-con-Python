from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

url = "https://dgrgw.comarb.gob.ar/dgr/login.jsp"

# Esta opcion es para que el navegador no  ejecute la interfaz grafica
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# self.bot = webdriver.Firefox(options=options)
"""
option = webdriver.FirefoxOptions.add_argument("--headless")
driver = webdriver.Firefox(options=option)
"""

# driver = webdriver.Firefox()
# driver.get(url)


def data_for_login():
    user = os.environ.get("COMARB_USER")
    password = os.environ.get("COMARB_PASSWORD")
    return user; password  # retorna una tupla()


 # de esta manera el 1° elemento de la tupla se asigna a la 1° variable
 # y asi con la 2° variable y el 2° valor de retorno de la funcion
user; password = data_for_login()
print("usuario:" + data_for_login()[0])
print("contraseña:" + data_for_login()[1])
