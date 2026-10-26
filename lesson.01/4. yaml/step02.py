import yaml


report = {
    'shop':
        {
            'name': 'ШИФТ Маркет',
            'enable': True,
            'discount': 0.1,
            'categories': ['Книги', 'Тетради'],
            'manager': None
        },
    'user':
        {
            'name': 'Bob',
            'is_active': True,
            'price': 10000,
            'prof': ['IT', 'Sale'],
            'admin': True
        }
}

with open('example.yaml', 'w', encoding="utf-8") as file:
    yaml.safe_dump(
        report,
        file,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )