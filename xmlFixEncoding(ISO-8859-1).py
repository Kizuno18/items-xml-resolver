import io
import re
from html import unescape
import xml.etree.ElementTree as ET

def fix_encoding(text):
    text = unescape(text)
    text = re.sub(r'&#(\d+);', lambda match: chr(int(match.group(1))), text)
    text = text.encode('iso-8859-1').decode('utf-8')
    return text

def fix_xml_encoding(xml_str):
    root = ET.fromstring(xml_str)
    for item in root.iter('item'):
        for attribute in item.iter('attribute'):
            attribute_value = attribute.get('value')
            fixed_value = fix_encoding(attribute_value)
            attribute.set('value', fixed_value)
    return ET.tostring(root, encoding='utf-8').decode('utf-8')

# Exemplo de uso:
with io.open('items_fixed.xml', 'r', encoding='utf-8') as f:
    xml_str = f.read()

fixed_xml_str = fix_xml_encoding(xml_str)

with io.open('items_fixed2.xml', 'w', encoding='utf-8') as f:
    f.write(fixed_xml_str)
