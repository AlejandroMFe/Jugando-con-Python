# Herencia
# crear una neuva clase a 
# partir de una ya existente

class Pokemon:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return f"Nombre: {self.nombre} de tipo: {self.tipo}"
    

class Picachu(Pokemon):
    # esta clase es hijo de la clase Pokemon
    # de la cual hereda todo

    def ataque(self, tipo_ataque):
        return f"{self.nombre} tipo de ataque {tipo_ataque}"

class Charmander(Picachu):
    # esta clase sería nieto de Pokemon
    # ya que Hereda de Pikachu
    # Pokemon
    #     -> Picachu 
    #           -> Charmander
    pass

joaquin = Picachu("Joaquin","electrico")
print(joaquin.nombre, "de tipo ", joaquin.tipo)
print(joaquin.ataque("ladrido"),"\n")

sofia = Charmander("Sofia", "fuego")
print(sofia.nombre, " de tipo ", sofia.tipo)
print(sofia.ataque("persecucion"))