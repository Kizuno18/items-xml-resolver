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
    # removemos valores duplicados
    attributes = list(set(attributes))

    # encontrando os atributos em sub-tags
    attribute_values = []
    for attribute in item.findall('.//attribute'):
        attribute_key = attribute.get('key')
        attribute_value = attribute.get('value')
        if attribute_key and attribute_value:
            attribute_values.append(f"{attribute_key}: {attribute_value}")

    print(f"Atributos para o item com ID {item.get('id')}: {attributes + attribute_values}")
