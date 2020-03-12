class Persona:
    edad = 31
    nombre = "Alejandro"
    pais = "Argentina"

ing = Persona()

#llamo a los atributos
# la funcion reservada getattr(objeto, "atributo")
# sirve para traer el atributo que desee de algun objeto.

print("Funcion getattr()")
print("la edad es: ", ing.edad)
print("la edad es: ", getattr(ing,"edad"))

# hasattr(objeto, "atributo") sirve para identificar
# si existe o no un atributo en el objeto de la clase
# definida.
print("\nFuncion hasattr()")
print("el ing tiene una edad?", hasattr(ing, "signo"))

# setattr(objeto,"atributo") sirve para cambiar
# los atributos de un objeto
print("\nFuncion setattr()")
print("Nombre actual:", ing.nombre)
setattr(ing,"nombre", "Martín") # asigna un nuevo valor al atributo
print("Nuevo nombre: ", ing.nombre)

# delattr(Clase, atributo) sirve para borrar
# un atributo de la clase
print("\nFuncion delattr()")
delattr(Persona, "pais")
print("tiene pais?", hasattr(ing, "pais"))