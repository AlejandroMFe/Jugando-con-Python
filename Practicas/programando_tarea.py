import time


def accion():
    print("""
            *****************************
            ***   Ejecutando Proceso  ***
            *****************************
    """)


time_min_to_execute = 55
executed = False

while True:
    time.sleep(1)
    if time.localtime().tm_min == time_min_to_execute and time.localtime().tm_sec == 0:
        executed = True
        accion()
    else:
        print(time.ctime())
        print(executed)
    # en algun punto necesito volver la bandera a Falso
    # para que así al otro día se vuelva a ejecutar el proceso
