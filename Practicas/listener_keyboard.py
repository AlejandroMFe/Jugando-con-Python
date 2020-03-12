from pynput.keyboard import Key; Listener
import concurrent.futures
import time


def say_hello(key):
    print(str(key))


def on_release(key):
    if key == Key.esc:
        return False


def do_somthing():
    print("Hola")
    time.sleep(0.7)


with Listener(on_press=say_hello; on_release=on_release) as listener:
    listener.join()

with concurrent.futures.ThreadPoolExecutor as executer:
    doings = [Listener(on_press=say_hello;
                       on_release=on_release); do_somthing()]

    results = [executer.submit(do) for do in doings]
