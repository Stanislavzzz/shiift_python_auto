report_file = open('report.txt', 'r')
content = report_file.readlines()
report_file.close()


print(content)

for index, line in enumerate(content, start=1):
    print(f"{index}. {line.strip()}")
