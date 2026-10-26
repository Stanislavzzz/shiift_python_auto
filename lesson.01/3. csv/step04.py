import csv


data = [
    {'Имя': 'Иван', 'Возраст': '23', 'Город': 'Москва'},
    {'Имя': 'Боб', 'Возраст': '12', 'Город': 'Сочи'},
    {'Имя': 'Анна', 'Возраст': '32', 'Город': 'Тула'},
]


with open('data_names_dict.csv', 'a', newline='', encoding='utf-8') as csvfile:

    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


    for row in data:
        writer.writerow(row)
