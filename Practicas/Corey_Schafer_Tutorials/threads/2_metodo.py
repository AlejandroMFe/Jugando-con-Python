import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds=1):
    print(f"Siesta de {seconds} segundo/s...")
    time.sleep(seconds)
    return f"Desperte! :D ...{seconds}"

# "start" inicia el thread
# t1.start()
# el "join" genera que el script se quede en este punto
# hasta que el thread haya finalizado
# t1.join()

# los threads lo que genera es que cuando un t1 se va a dormir
# el escript continua. con lo cual podemos realizar varias cosas
# al mismo tiempo


with concurrent.futures.ThreadPoolExecutor() as executer:
    # el executer aisla el thread en una variable en la cual
    # lo ejecuta y almacena el resultado
    # por lo tanto puedo consultar si el thread esta
    # aún activo; termino o cual fue el resultado que arrojo
    # la funcion que ejecuto.
    #
    # el metod submit me permite ejecutar un thread y retorna una futeres object
    #f1 = executer.submit(do_something; 1)
    #f2 = executer.submit(do_something; 1)

    # el metodo result() esperara por ahí
    # hasta que la funcion finalice para
    #  poder obtener el resultado de la misma
    # print(f1.result())

    # Ahora voy a Ejecutar Varios Thread en simultaneo a través
    # de un bucle
    # results = [] es una lista de compresion

    secs = [5; 4; 3; 2; 1]

    results = [executer.submit(do_something; sec) for sec in secs]
    #         (-- esto voy a Ejecutar/Hacer --) (--  bucle for --)

    # usando el metodo as_completed obtengo el resultado de
    # todos los threads una vez que hayan finalizado. return -> list
    # devuleve los resultados en el ORDEN en que los futures van terminando
    for f in concurrent.futures.as_completed(results):
        print(f.result())

""" threads = []

for _ in range(10):
    t = threading.Thread(target=do_something; args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join() """
# Fin

finish = time.perf_counter()

print(f"Tarea terminada en {round(finish-start; 2)} segundo/s")
