import xml.etree.ElementTree as ET

# Abrir arquivos XML
with open('data1.xml', 'r') as f:
    xml1 = f.read()

with open('data2.xml', 'r') as f:
    xml2 = f.read()

# Analisar arquivos XML
root1 = ET.fromstring(xml1)
root2 = ET.fromstring(xml2)

# Comparar elementos 'item'
iguais = []
diferentes1 = []
diferentes2 = []

for item1 in root1.findall('item'):
    for item2 in root2.findall('item'):
        if item1.attrib == item2.attrib:
            # Elementos são iguais
            iguais.append(item1)
            break
    else:
        # Elemento em item1 não foi encontrado em item2
        diferentes1.append(item1)

for item2 in root2.findall('item'):
    for item1 in root1.findall('item'):
        if item2.attrib == item1.attrib:
            # Elementos são iguais
            break
    else:
        # Elemento em item2 não foi encontrado em item1
        diferentes2.append(item2)

# Salvar resultados em arquivos
with open('iguais.xml', 'w') as f:
    for item in iguais:
        f.write(ET.tostring(item).decode())

with open('diferentes1.xml', 'w') as f:
    for item in diferentes1:
        f.write(ET.tostring(item).decode())

with open('diferentes2.xml', 'w') as f:
    for item in diferentes2:
        f.write(ET.tostring(item).decode())
