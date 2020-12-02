import send_email
import datetime
import chromedriver_binary
from datetime import timedelta
from comarb_class import Comarb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def enable_download_in_headless_chrome(browser, download_dir):
    # Esta funcion permite que el chrome descargue un archivo
    # de manera automatica sin pregutnar si lo desea descargar
    # add missing support for chrome "send_command"  to selenium webdriver
    # by https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c86
    browser.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def set_options_webdriver(download_dir):
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-gpu")
    browser_options.binary_location = "D:\\Development\\Resources\\GoogleChromePortable83\\App\\Chrome-bin\\chrome.exe"
    prefs = {"download.default_directory": download_dir,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enable": True,
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs", prefs)
    return browser_options


comarb = Comarb()

browser_options = set_options_webdriver(download_dir=comarb.download_dir)
browser = webdriver.Chrome(options=browser_options)
enable_download_in_headless_chrome(browser, comarb.download_dir)


# Recibo la fecha :str y la transformo a objeto datetime
# str -> datetime
# dd/mm/YYYY -> date(YYYY, mm, dd)
last_file_processed = comarb.get_date_last_file_processed(browser)
day = last_file_processed[:2]
month = last_file_processed[3:5]
year = last_file_processed[6:]
object_last_file = datetime.date(int(year), int(month), int(day))

# obtengo la fecha de ayer
yesterday = datetime.date.today() - timedelta(1)
comarb.recording("--> Yesterday: {}".format(str(yesterday)))

try:
    # Va buscar, descargar y subir los archivos que falten
    # hasta que la fecha del ulrimo archivo procesado
    # sea igual que la fecha de ayer, que representa el
    # ultimo archivo que han subido en Comarb.
    # Pd: los archivos son procesados con un día de anterioridad
    # osea ayer al día actual de hoy.
    while object_last_file < yesterday:
        # incremento un dia a la fecha del ultio archivo procesado
        object_last_file += timedelta(1)

        # le paso las fecha: str del archivo que necesita
        # buscar y descargar
        comarb.set_xml_filename(str(object_last_file))
        comarb.download_file_comarb(browser)
        comarb.upload_file_atp(browser)
    comarb.recording("--> Estamos al día")
    #send_email.send("EXitoo!!", comarb.log)

except TimeoutException as e:
    comarb.recording(str(e))
    send_email.send("Wep! Algo paso XD", comarb.log)

except Exception as e:
    comarb.recording(str(e))
    send_email.send("Wep! Algo paso XD", comarb.log)

finally:
    browser.quit()
