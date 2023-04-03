import xml.etree.ElementTree as ET

# carrega o arquivo XML
tree = ET.parse('items.xml')
root = tree.getroot()

# define uma função para extrair o ID de um elemento "item"
def get_item_id(elem):
    item_id = elem.get('id')
    if item_id:
        return int(item_id)
    from_id = elem.get('fromid')
    if from_id:
        return int(from_id)
    to_id = elem.get('toid')
    if to_id:
        return int(to_id)
    return None

# ordena os elementos "item" por ID
sorted_elements = sorted(root.findall('item'), key=get_item_id)

# substitui os elementos antigos pelos novos elementos ordenados
for i, elem in enumerate(sorted_elements):
    root[i] = elem

# salva o arquivo XML ordenado
tree.write('items_sorted.xml')
