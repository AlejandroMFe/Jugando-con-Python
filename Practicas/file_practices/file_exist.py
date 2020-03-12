from pathlib import Path
from time import sleep

path_filename = "D:\\OneDrive\\Jugando con Python\\Practicas\\file_practices\\XML_definitivo_906_2020-02-17.xml"
chrome_download_extension = ".crdownload"


steel_download_file = path_filename + chrome_download_extension
steel_download_path = Path(steel_download_file)

while steel_download_path.exists():
    sleep(1)
    print("Descargando..")

path = Path(path_filename)
if path.exists() and path.is_file():
    print("Archivo Si existe")        
else:
    print("Archivo No existe")        
