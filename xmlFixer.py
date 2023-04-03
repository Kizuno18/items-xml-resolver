import re
import xml.etree.ElementTree as ET

# Lê o arquivo XML de entrada
tree = ET.parse("diferentes2.xml")
root = tree.getroot()

# Regex para extrair os ids separados por traços
regex = re.compile(r'(\d+)-(\d+)')

# Itera sobre todos os elementos 'item'
for item in root.findall('.//item'):
    # Obtém o id do item
    item_id = str(item.get('id'))
    
    # Verifica se o id contém traços
    match = regex.match(item_id)
    if match:
        # Extrai os ids separados por traços
        fromid = match.group(1)
        toid = match.group(2)
        
        # Adiciona os atributos 'fromid' e 'toid' no elemento 'item'
        item.set('fromid', fromid)
        item.set('toid', toid)
        
        # Remove o atributo 'id' do elemento 'item'
        del item.attrib['id']

# Salva o arquivo XML modificado
tree.write("output.xml")
