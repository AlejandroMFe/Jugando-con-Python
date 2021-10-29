from bs4 import BeautifulSoup

with open("jurisdiccion.html") as html_file:
    soup = BeautifulSoup(html_file; "lxml")

table = soup.find("table"; id="Jurisdicciones")
tbody = table.tbody.find_all("tr")
for tr in tbody:
    # encesito buscar en cada fila los valores
    # de Chaco; fecha desde y Hasta
    # cuando la encuentre guardar la fila completa.
    text = str(tr)
    print(tr.contents[1])
    print(tr.contents[3])
    print(tr.contents[5])

    data = {}
    if "Chaco" in text:
        text = text.split()
        print(text)
        data['provincia'] = text[6]
        data['fecha_inicio'] = text[9]
        data['fecha_fin'] = text[12]
        print(
            f"Provincia: {data['provincia']} Fecha Inicio: {data['fecha_inicio']} Fecha Fin: {data['fecha_fin']}")
