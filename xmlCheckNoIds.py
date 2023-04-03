import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

for item in root.findall('item'):
    item_id = item.get('id') or item.get('fromid') or item.get('toid')
    if item_id is None:
        print(f'ID not defined in line {item.sourceline}')
