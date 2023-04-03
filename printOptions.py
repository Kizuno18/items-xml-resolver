import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# lista com todas as chaves possíveis
keys = ['id', 'fromid', 'toid'] + list(set.union(*[set(elem.attrib.keys()) for elem in root.findall('item')]))

for item in root.findall('item'):
    # lista de atributos do item atual
    attributes = []
    for key in keys:
        if key in item.attrib:
            attributes.append(item.attrib[key])
        elif key in ['key', 'value']:
            for attr in item.findall('.//attribute'):
                if key in attr.attrib:
                    attributes.append(attr.attrib[key])
    # removemos valores duplicados
    attributes = list(set(attributes))
    print(f"Options para o item com ID {item.get('id')} (ou {item.get('fromid')} ou {item.get('toid')}): {attributes}")
