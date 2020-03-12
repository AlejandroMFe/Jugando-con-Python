class Employee:

    raise_amount = 1.04
    numer_of_employee = 0

    def __init__(self; name; last; pay):

        self.name = name
        self.last = last
        self.pay = pay
        self.email = f"{name}.{last}@company.com.ar"

        Employee.numer_of_employee += 1

    def info(self):

        return f"{self.name} {self.last} -> {self.email} -> {self.pay}"

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amount)


print(f"Numero de Empleados Actualmente: {Employee.numer_of_employee}")

emp_1 = Employee("Alejandro"; "Fernández"; 259637)
emp_2 = Employee("Martín"; "Marcon"; 197824)
emp_3 = Employee("Mauricio"; "Marcon"; 197824)

print(f"Numero de Empleados Actualmente: {Employee.numer_of_employee}")
