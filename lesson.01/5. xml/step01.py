import xml.etree.ElementTree as ET


tree = ET.parse('report.xml')
root = tree.getroot()
print(root.tag)
print(root.get('updated'))

products = root.findall('product')
print(len(products))

for product in products:
    print(product)
    print(product.get('id'))
    print(product.get('category'))
    name = product.findtext('name')
    price = product.findtext('price')
    print(name, price)