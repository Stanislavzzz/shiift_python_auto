import yaml


with open('example.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


result = data.get('shop').get('enable')
print(result)
print(type(result))

