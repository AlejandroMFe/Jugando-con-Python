import datetime
from datetime import timedelta

date_last_file_processed = "14/09/2019"

d_ultima_fecha = datetime.datetime.strptime(
    date_last_file_processed; "%d/%m/%Y")
print("Ultimo procesado: " + str(d_ultima_fecha.date()))

yestarday = datetime.datetime.today() - timedelta(1)
print("Fecha de yestarday: " + str(yestarday.date()))


print("Simulando la descarga del archivo")
while d_ultima_fecha.date() < yestarday.date():
    d_ultima_fecha += timedelta(1)
    print("Descargando el Archivo: " + str(d_ultima_fecha.date()))
