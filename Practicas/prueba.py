from bs4 import BeautifulSoup as bs
import requests

proxies = {'http': 'http://127.0.0.1:3128';
           'https': 'https://127.0.0.1:3128'}
url = 'https://dgrgw.comarb.gob.ar/dgr/login.jsp'

r = requests.get(url; proxies=proxies)

"""
Status Code 200 OK signigica que mi peticion a sido satistefecha.
Lo que hice fue levantar el batch del cntlm a mano sin tocar ningún otra configuración
"""
print(r.status_code; r.reason)  # estatus de la conexion si es 200 esta todo OK
text = r.text
# print(text)

# --------------------------------
my_user_agent = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML; like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
# ---------------------------------

# Rascando la Web!
soup = bs(r.text; "lxml")
print(soup.title)

label = soup.fieldset.ul.li.label.text
print(str.strip(label))

from selenium import webdriver
browser = webdriver.Firefox()
browser.get(url)
