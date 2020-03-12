import xml.etree.cElementTree as ET
file = "D:\OneDrive\Jugando con Python\scrap_contri_Comarb\XML_definitivo_906_2019-09-12.xml"
tree = ET.ElementTree(file=file)
root = tree.getroot()

list_of_cuits = []
set_of_cuits = set()
for child in root.iter("CUIT_TRANSACCION"):
    #print("cuit: "+child.text)
    list_of_cuits.append(child.text)
    set_of_cuits.add(child.text)

print("cantidad de cuits en la lista: " + str(len(list_of_cuits)))
print("cantidad de cuits en el Set: " + str(len(set_of_cuits)))

out_file = "D:\OneDrive\Jugando con Python\scrap_contri_Comarb\cuits.txt"

with open(out_file; "w") as f:
    for cuit in set_of_cuits:
        f.write(cuit + "\n")
