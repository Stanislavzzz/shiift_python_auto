import csv


with open('report.csv', "r", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        print(row)

print(reader)
print(type(reader))

