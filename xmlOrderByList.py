import xml.etree.ElementTree as ET

# Define a ordem dos atributos
attribute_order = [
     'skillFist',
    'skillDist',
    'skillShield',
    'skillSword',
    'skillAxe',
    'skillClub',
    'magicpoints',
    'extradef',
    'slotType',
    'preventDrop',
    'armor',
    'defense',
    'speed',
    'containerSize',
    'worth',
    'absorbPercentLifeDrain',
    'showcharges', 'absorbPercentEnergy', 'charges', 'showattributes',
    'absorbPercentPhysical', 'absorbPercentHoly', 'absorbPercentDeath', 'absorbPercentIce', 'absorbPercentFire', 'absorbPercentEarth',
    'showduration', 'transformEquipTo',
    'absorbPercentPoison',
    'absorbPercentManaDrain',
    'manaGain', 'healthGain', 'manaTicks', 'healthTicks',
    'maxHitChance',
    'elementDeath',
    'absorbPercentAll',
    'magiclevelpoints',
    'elementEnergy',
    'elementHoly',
    'reflectchanceall', 'reflectpercentall',
    'elementFire',
    'elementIce',
    'elementEarth',
    'ammoType',
    'showcount',
    'fluidSource', 'corpseType',
    'absorbPercentDrown',
    'hitChance',
    'floorchange', 'decayTo', 'duration',
    'rotateTo',
    'specialDoor',
    'closingDoor',
    'levelDoor',
    'text',
    'readable',
    'description',
    'writeable', 'maxTextLen',
    'weight',
    'cache',
    'start',
    'suppressDrunk',
    'usetimebetweenexactions',
    'pickupable',
    'invisible',
    'walkStack',
    'blocksolid',
    'type', 'effect', 'allowpickupable',
    'fieldAbsorbPercentFire',
    'manashield',
    'runeSpellName',
    'damage', 'count', 'replaceable', 'field', 'ticks',
    'stopduration',
    'forceSerialize',
    'writeOnceItemId',
    'attack', 'weaponType', 'shootType', 'ammoAction', 'range', 'breakChance',
    'blockprojectile',
    'femaleTransformTo', 'partnerDirection', 'maleTransformTo',
    'transformTo',
    'transformUseTo'
]

# Função para obter a chave de classificação de um item
def item_sort_key(item):
    # Obtém a lista de chaves de atributos do item
    item_attribute_keys = [attribute.get('key') for attribute in item.findall('.//attribute')]
    # Obtém a lista de índices de ordem de atributos para cada chave de atributo
    item_attribute_indices = [attribute_order.index(key) for key in item_attribute_keys if key in attribute_order]
    # Retorna a lista de índices de ordem de atributos, garantindo que os itens sem atributos ordenados apareçam no final
    return item_attribute_indices if item_attribute_indices else [len(attribute_order)]

# Abre o arquivo XML e obtém o elemento raiz
tree = ET.parse('items.xml')
root = tree.getroot()

# Obtém a lista de itens e os ordena usando a função de classificação
items = root.findall('.//item')
items_sorted = sorted(items, key=item_sort_key)

# Remove todos os itens existentes da raiz
for item in items:
    root.remove(item)

# Adiciona os itens ordenados de volta à raiz
for item in items_sorted:
    root.append(item)

# Salva o arquivo XML de volta no disco
tree.write('items.xml')
