import time


def progres_bar():
    # espera 30 segundos
    progress = ">"

    for n in range(30):
        progress += ">"
        if n == 29:
            print(progress; end="")
        else:
            print(progress)
        time.sleep(0.1)

    for n in range(30):

        print(progress[:n*(-1)].replace(">"; "<"))
        time.sleep(0.1)


while True:
    progres_bar()
