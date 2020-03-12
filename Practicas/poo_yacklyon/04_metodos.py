# Metodos

# class Persona:
#     nombre = "Alejandro"

#     def mi_nombre(self):
#         return self.nombre

# p1 = Persona()
# print(p1.mi_nombre())

# class Matematica:
#     def suma(self):
#         self.nro1 = 6
#         self.nro2 = 6

# operacion = Matematica()
# # llama primero al metodo para luego poder
# # acceder a sus atributos o variables.
# operacion.suma() 
# print(operacion.nro1 + operacion.nro2)

# ---> Metodo __init__

# class Ropa:
#     def __init__(self):
#         self.marca = "willow"
#         self.talla = "L"
#         self.color = "blue"

# remera = Ropa()
# camisa = Ropa()
# camisa.color = "blanca"
# camisa.marca = "Alejandro"
# camisa.talla = "XL"

# print(f"Marca: {remera.marca}")
# print(f"Talla: {remera.talla}")
# print(f"Color: {remera.color}\n")
# print(f"Marca: {camisa.marca}")
# print(f"Talla: {camisa.talla}")
# print(f"Color: {camisa.color}")

class Calculadora:
    def __init__(self, nro1:int , nro2:int):
        # estos son Atributos de la Clase
        self.suma = nro1 + nro2
        self.resta = nro1 - nro2
        self.multiplicacion = nro1 * nro2
        self.division = nro1 / nro2

operacion = Calculadora(3,4)
print(operacion.resta)