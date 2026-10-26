import csv


data = [
    ['Имя', 'Возраст', 'Город'],
    ['Иван', '23', 'Москва'],
    ['Боб', '12', 'Сочи'],
    ['Анна', '32', 'Тула'],
]


with open('data_names.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')

    for row in data:
        writer.writerow(row)
