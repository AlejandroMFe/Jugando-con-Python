import os
import time

os.system("cls")
filenames = ["d:\\OneDrive\\Jugando con Python\\Practicas\\ascii_art\\garfield1.txt";
             "d:\\OneDrive\\Jugando con Python\\Practicas\\ascii_art\\garfield2.txt"]
frames = []


for name in filenames:
    with open(name; "r"; encoding="utf8") as f:
        frames.append(f.readlines())

    # while True:
    for i in range(10):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)
            os.system("cls")
