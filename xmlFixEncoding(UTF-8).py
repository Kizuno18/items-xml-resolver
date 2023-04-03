import xml.etree.ElementTree as ET
import re

def fix_encoding(string):
    # Substitui os caracteres incorretos pelos corretos
    string = re.sub(r"Ã¡", "á", string)
    string = re.sub(r"Ã©", "é", string)
    string = re.sub(r"Ã­", "í", string)
    string = re.sub(r"Ã³", "ó", string)
    string = re.sub(r"Ãº", "ú", string)
    string = re.sub(r"Ã£", "ã", string)
    string = re.sub(r"Ã§", "ç", string)
    string = re.sub(r"Ã€", "À", string)
    string = re.sub(r"Ã‰", "É", string)
    string = re.sub(r"Ã“", "Ó", string)
    string = re.sub(r"Ãš", "Ú", string)
    string = re.sub(r"Ã‚", "Â", string)
    string = re.sub(r"ÃŠ", "Ê", string)
    string = re.sub(r"Ã”", "Ô", string)
    string = re.sub(r"Ãƒ", "Ã", string)
    string = re.sub(r"Ã‡", "Ç", string)
    return string

# Abre o arquivo XML
tree = ET.parse('items.xml')
root = tree.getroot()

# Percorre todos os elementos e atributos, corrigindo as codificações
for elem in root.iter():
    for key, val in elem.attrib.items():
        elem.attrib[key] = fix_encoding(val)

# Salva o arquivo XML corrigido
tree.write('items_corrigido.xml', encoding='utf-8')
