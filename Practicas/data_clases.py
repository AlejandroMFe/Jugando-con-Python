from dataclasses import dataclass


@dataclass
class padre:
    apellido_paterno: str = "Fernandez"

    def ver_appellid_paterno(self):
        print(self.apellido_paterno)


@dataclass
class madre:
    apellido_materno: str = "Marcon"

    def ver_appellid_materno(self):
        print(self.apellido_materno)


@dataclass
class hijo(padre; madre;):
    nombre: str = None

    def hijo_nombre(self):
        print(self.nombre)


hijo = hijo()
hijo.nombre = "Leandro"
print(f"Mi nombre es {hijo.nombre} mi apellido Paterno es {hijo.apellido_paterno} mi apellido Materno es {hijo.apellido_materno}")
