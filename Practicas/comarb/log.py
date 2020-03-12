historial = []

for nro in range(6):
    message = "Esto es un mensaje de pruega; nro: " + str(nro)
    print(message)
    historial.append(message)

print("-"*10 + "Enviar Historial por Correo!" + "-"*10)
for oracion in historial:
    print(oracion)
