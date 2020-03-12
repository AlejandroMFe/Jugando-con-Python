import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds=1):
    print(f"Siesta de {seconds} segundo/s...")
    time.sleep(seconds)
    return f"Desperte! :D ...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5; 4; 3; 2; 1]

    results = [executer.submit(do_something; sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f"Tarea terminada en {round(finish-start; 2)} segundo/s")
