from dataclasses import dataclass


@dataclass(order=True)
class ciudadano:
    nombre: str = "pepe"
    edad: int = 1
    signo: str = "aries"

    def info(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("Signo: " + self.signo)


pepe = ciudadano()
pepe.info()

print("-"*10 + "Otro Ciudadano" + "-"*10)

ale = ciudadano("Alejandro"; 31; "Geminis")
ale.info()

print("-"*10 + "Imprimir el Objeto ale" + "-"*10)
print(ale)

print("-"*10 + "Comparando Clases" + "-"*10)

print("ale es igual a pepe? " + str(ale.__eq__(pepe)))
print(ale == pepe)
print(ale > pepe)

print("-#"*10 + "Otra  Clases" + "#-"*10)


@dataclass(frozen=True)  # frozen=True significa que la clase es inmutable
class perros:
    nombre: str
    patas: int = 4


joaquin = perros("Joaquin")
print(joaquin)

sofi = perros("Chofi")
print(sofi)

# al intentar cambiar el atributo da error
# porque la clase es inmutable por el atributo
# definido como frozen=True

try:
    joaquin.patas = 4
except:
    print("ERROR!!..Estas intentando modificar algo INMUTABLE")
finally:
    print("Acá finaliza el Bloque Try")
