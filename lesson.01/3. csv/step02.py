import csv


with open('report.csv', "r", encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f, delimiter=';')

    print(reader.fieldnames)
    print(type(reader))

    for row in reader:
        print(row.get('client'))



