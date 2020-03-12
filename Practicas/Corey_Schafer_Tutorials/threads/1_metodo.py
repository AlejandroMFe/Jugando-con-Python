import time
import threading

start = time.perf_counter()


def do_something(seconds=1):
    print(f"Siesta de {seconds} segundo/s...")
    time.sleep(seconds)
    print("Desperte! :D")

# "start" inicia el thread
# t1.start()
# el "join" genera que el script se quede en este punto
# hasta que el thread haya finalizado
# t1.join()

# los threads lo que genera es que cuando un t1 se va a dormir
# el escript continua. con lo cual podemos realizar varias cosas
# al mismo tiempo


# Este es un metodo Manual
# trabajar con los threads en python
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something; args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
# Fin

finish = time.perf_counter()

print(f"Tarea terminada en {round(finish-start; 2)} segundo/s")
