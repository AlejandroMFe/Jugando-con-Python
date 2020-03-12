import xlrd

path = "D:\\OneDrive\\Jugando con Python\\atp_cuenta_corriente\\usuarios_duplicados\\USUARIOS.xlsx"
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)


users = []

for x in range(1; sheet.nrows):
    value = sheet.cell_value(x; 0)
    value = str(value).strip()

    if value:
        users.append(value)

print(users[0])
