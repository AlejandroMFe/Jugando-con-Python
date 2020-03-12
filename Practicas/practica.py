from dataclasses import dataclass
import mi_modulo

mi_modulo.bienvenida()


def una_funcion(numero: int) -> bool:
    if type(numero) == int:
        print("es un entero")
    else:
        print("NO es un enter")


una_funcion("8")



