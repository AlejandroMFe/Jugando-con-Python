# metodo constructor

class Persona:

    def __init__(self, nombre, año):
        # self.nombre es un atributo/propiedad de la clase
        self.nombre = nombre # nombre es un valor que recibe la Clase
        self.año = año

    def descripcion(self):
        # return retorna un valor o algo desde la funcion
        return "{} tiene {} años".format(self.nombre, self.año)

    def comentario(self, frase):
        # frase es un valor que recibe el metodo
        return f"{self.nombre} dice: {frase}"

coach = Persona("Alejandro", 31)

# print(coach.descripcion())
# print(coach.comentario("Me gusta mucho Python"))


# modificar los atributos/propiedades de la clase -> objeto

class Email:
    def __init__(self):
        self.enviado = False
    
    def enviar_correo(self):
        # modifico el valor del atributo desde el metodo
        # para ello uso el self, haciendo referencia 
        # al atributo de la clase
        self.enviado = True

mi_correo = Email()

print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)