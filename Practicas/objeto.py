class persona:

    def __init__(self; nombre="Tito"; signo="Acuario"; edad=20):
        self.name = nombre
        self.signo = signo
        self.edad = edad

    def print_info(self):
        print(self.name)
        print(self.signo)
        print(str(self.edad))


persona_prueba = persona()
print("--- Objeto con Valores Predetermindas ---")
persona_prueba.print_info()

print("--- Inicializando un Objeto con Pasando Valores ---")
persona_uno = persona(nombre="Alejandro"; signo="Geminis"; edad=31)
persona_uno.print_info()
