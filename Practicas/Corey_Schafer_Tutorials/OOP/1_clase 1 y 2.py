

class Employee:
    # estas son Variables de la CLASE
    raise_amount = 1.04
    numer_of_employee = 0

    # esta es la clase
    # la cual recibe de manera automatica; siempre; el primer argumenteo
    # "self" el cual hace referencia a la intancia

    # los metodos toman automaticamente la INSTANCIA de la CLASE como primer parametro ose "self"
    def __init__(self; name; last; pay):
        """el __init___ metodo corre siempre al inicio cuando se instancia un objeto de la CLASE"""
        # estas son Variables de INSTANCIA
        self.name = name
        self.last = last
        self.pay = pay
        self.email = f"{name}.{last}@company.com.ar"
        # aqui me aseguro de que solo se incremente el valor cuando se Intancia un nuevo objeto de la clase Employee
        # por eso tambien llamo a la CLASE y NO uso self para que el valor sea una constante diferente entre cada
        # instancia de Employee
        Employee.numer_of_employee += 1

    # un método es una Funcion que corresponde a una clase
    # Metodo = Funcion -> Clase
    # osea que la funcion que pertence a la clase se llaman Métodos
    # y las variables que corresponeden a una Clase son Atributos.
    def info(self):
        # la instancia "self" se pasa automáticamente siempre.
        return f"{self.name} {self.last} -> {self.email} -> {self.pay}"

    def apply_raise(self):
        # self.raise_amount estoy accediendo a una variable de la clase
        self.pay = int(self.pay * self.raise_amount)


print(f"Numero de Empleados Actualmente: {Employee.numer_of_employee}")
# esta es una instancia de la clase osea un objeto del tipo Employee
emp_1 = Employee("Alejandro"; "Fernández"; 259637)
emp_2 = Employee("Martín"; "Marcon"; 197824)
emp_3 = Employee("Mauricio"; "Marcon"; 197824)
print(f"Numero de Empleados Actualmente: {Employee.numer_of_employee}")


""" lo que realmente ocurre cuando se pasa la instancia de manera automatica es lo siguiente
 Acá estoy llamando  a la Clase pero necesito decirle a cual Instancia me refiero
 por lo cual debo señalarsela
 emp_2 es el parametro "self" que menciono en la clase que es pasado automáticamente exceptuando este ejemplo"""
# print(Employee.info(emp_2))
"""eso ocurre cuando yo llamo al metodo desde la instancia de la clase...
a eso me refiero cuando la instancia; el primer atributo; se pasa automáticamente"""
# print(emp_2.info())

""" las dos variantes generan el mismo resultado. Pero una es llamando a la Clase y pasando la Instancia
  y la otra es desde la Instancia llamando al Método"""

# print(Employee.__dict__)
""" como emp_1 no tiene definidio la variable raise_amount (aumento de sueldo)
 lo que hace la instancia es ir a la clase y tomar el valor que esta almacena en la variable raise_amounte de la clase"""
# print(emp_1.__dict__)

"""
Las instancias de una Clase los valores de las variables que tiene la clase a menos que estas variables
sean defininas en la instancia como ocurre en el caso del emp_2.raise_amount que defino su valor y 
solo cambia el valor para esa instancia de la clase.
"""
print(Employee.raise_amount)
emp_2.raise_amount = 1.05
print(emp_2.raise_amount)
print(emp_1.raise_amount)
