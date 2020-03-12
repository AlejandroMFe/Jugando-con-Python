from dataclasses import dataclass


@dataclass
class perro():
    raza: str
    nombre: str
    color: str

    def guaf(self):
        print(
            f"Mi nombre es: {self.nombre}\n"
            f"Mi raza es: {self.raza}\n"
            f"Mi color es: {self.color}\n"
        )
        print("Guaf! Guaf! Guaf!")
