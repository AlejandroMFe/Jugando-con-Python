try:
    """Mensaje de error al NO encontrar el elemento de j_username.
    Necesito ponerlo en un try para capturar la situación
    En caso de haber erro necesito cerrar el navegador y terminar el programa
    selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="j_username"]"""
    input_usuario = browser.find_element_by_id("j_username")
    print("input")
    print(input)
    input_password = browser.find_element_by_id("j_password")
except EC.NoSuchElementException:
    print("NO se encontro el elemento")
    browser.quit()
    # !TODO enviar email informando el fallo del sistema.
    print("Sending Email...")
    print("Cerrar el Sistema")
    sys.exit()


<div class = "texto_cajas_home" >
USUARIO: afernandez
</div >

# ------------ Importando el archivo en ATP
# ------Boton Explorar
<input id = "fileuploadUPLOADIFY2Container" type = "file" name = "files[]" >

# -----Boton Importar
<input type = "button" name = "BTNIMPORTAR"
value = "Importar" title = "Importar"


class = "SpecialButtons" style = ""


onclick = "if( gx.evt.jsEvent(this)) {gx.evt.execEvt('E\'IMPORTAR\'.';this);} else return false;"
onfocus = "gx.evt.onfocus(this; 47;'';false;'';0)" >

# ------Boton Procesar Archivo
<input type = "button" name = "BUTTON1" value = "Procesar Archivo" title = "Procesar Archivo"


class = "SpecialButtons" onclick = "if( gx.evt.jsEvent(this)) {gx.evt.execEvt('E\'PROCESAR\'.';this);} else return false;"


onfocus = "gx.evt.onfocus(this; 9;'';false;'';0)" >


""" Esta configuracion de perfil de FireFox es para que
descague todos los archivos .xml sin pregutnar
donde guardarlos.

profile = webdriver.FirefoxProfile()
# le dice que NO use el directorio de descargas por defecto
profile.set_preference("browser.download.folderList"; 2)
# Que NO muestre el administrador de Descargas
profile.set_preference("browser.download.manager.showWhenStarting"; False)
# Le paso el directorio donde se va a guardar el archivo
profile.set_preference("browser.download.dir";
                       "D:\\Descargas\\comarb_descargas")
# Para todos los archivos xml que NUNCA pregunte y los guarde
# directamente en el disco
profile.set_preference("browser.helperApps.neverAsk.saveToDisk";
                       "application/xml")
"""

"""options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Ejecutar FireFox SIN interfaz Grafica

browser = webdriver.Firefox(options=options)
browser.get(url)
"""
