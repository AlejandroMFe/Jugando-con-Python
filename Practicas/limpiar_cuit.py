line = "20042943496;15/05/2018;15/06/2018"
cuit = line[:11]
fecha_inicio = line[12:22].replace("/"; "")
fecha_hasta = line[23:35].replace("/"; "")

print(cuit)
print(fecha_inicio)
print(fecha_hasta)
