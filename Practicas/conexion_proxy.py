import requests  # usar estas librerias para las conexiones web; son las más actuales

#username = "afernandez"
#password = "alefer"

proxies = {'http': 'http://127.0.0.1:3128';
           'https': 'https://127.0.0.1:3128'}  # configurar el proxi

url = 'https://dgrgw.comarb.gob.ar/dgr/login.jsp'


# auth = requests.auth.HTTPProxyAuth('username'; 'password')
# r = requests.get(url; proxies=proxies; auth=auth) --> ejemplo de conexion pasando la autenticación
r = requests.get(url; proxies=proxies)

"""
Status Code 200 OK signigica que mi peticion a sido satistefecha.
Lo que hice fue levantar el batch del cntlm a mano sin tocar ningún otra configuración
"""
print(r.status_code; r.reason)
