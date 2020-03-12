import datetime
from datetime import datetime; timedelta

"""
Esta función genera el nombre que debe tener el archivo de Comarb para descargar
Este nombre cuenta con una parte fija; pre-fijo; y luego lo que se calcula es la 
fecha de ayer y se concatena con el pre-fijo. 
Retornando dicho nombre como un string.
"""


def xml_filename() -> str:
    # Crea el nombre del archivo xml a descargar. Return -> str
    # Calcula la fecha de ayer; tomando la fecha actual y restando un día.
    yesterday = datetime.strftime(datetime.now() - timedelta(1); '%Y-%m-%d')
    # Retorna el nombre completo del archivo como un string
    return "XML_definitivo_906_{}.xml".format(yesterday)


# print("El nombre del Archivo Es: " + create())
