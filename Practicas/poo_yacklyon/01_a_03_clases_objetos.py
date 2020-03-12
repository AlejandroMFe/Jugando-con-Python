# clases son el molde del Objeto
# es como el molde para pasteleria donde 
# creo diferentes panes(objetos) con el mismo molde(clase)

class Auto:
    marca = ""
    modelo = 0
    placa = ""

taxi = Auto() # taxi es del molde(clase) Auto
#print(taxi.modelo)

# -- > clases y objetos 2

class persona:
    nombre= "Alejandro"
    edad = 31
    signo = "Geminis"

#print(persona.nombre)


class jugadores_a:
    # de esta manera los j1 y j2 son Objetos definidos
    j1 = "Alejandro" # objeto ya definido
    j2 = "Martín"

class jugadores_b:
    j1 = "Jose" 
    j2 = "Juan"

# print(jugadores_a.j1)
# print(jugadores_b.j1)

class nombre:
    pass

# objeto.atributo = valor
alejandro = nombre()
marisol = nombre()

# defino objetos de manera Estatida
# estos tambien son Objetos pero que 
# no puedo cambiar sus valores
alejandro.edad = 31
alejandro.signo = "Geminis"
alejandro.lenguaje_programacion = "Python & ASP.NET"

print(alejandro.signo)

