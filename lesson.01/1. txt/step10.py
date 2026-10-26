# report_file = open('report.txt', 'r')
# content = report_file.read()
# report_file.close()
#
# print(content)

with open('report.txt', 'r') as report_file:
    content = report_file.read()

print(content)