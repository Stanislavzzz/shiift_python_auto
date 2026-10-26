report_file = open('report.txt', 'r', encoding='utf-8')

line = report_file.readline()
# print(line)
# print("*" * 50)
# line = report_file.readline()
# print(line)

while line:
    print(line)
    print("*" * 50)
    line = report_file.readline()

report_file.close()


