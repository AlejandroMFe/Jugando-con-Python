from pynput.keyboard import Key; Listener
import time


def on_press(key):
    print(f"{key} pressed")


def on_release(key):
    print(f"{key} relesed")
    if key == Key.esc:
        # Stop listener

        return False


# Collect events until released
with Listener(on_press=on_press; on_release=on_release) as listener:
    # listener.start()
    oracion = " esta es una oracion que puede ser tratada como una Lista en Python!"
    for letter in oracion:
        print(letter)
        time.sleep(0.6)
