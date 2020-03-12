with open("data.txt", "w") as f:
    for i in range(11):
        f.write("Creado Fake data -> {}\n".format(i))

with open("scrap_contri_Comarb\\cuits.txt", "r") as f:
    print("Imprimiendo el contenido de data.txt")
    for line in f:
        print(line, end="")
