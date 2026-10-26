import yaml

yaml_text = """shop:
  name: ШИФТ Маркет
  enable: true
  discount: 0.1
  categories:
    - Книги
    - Тетради
  manager: null
"""

# yaml_text1 = """- Книги
#     - Тетради
# """

data = yaml.safe_load(yaml_text)
print(data)
print(type(data))

print(data['shop']['categories'])