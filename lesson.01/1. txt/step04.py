report_file = open('report.txt', 'r', encoding='utf-8')

# chunk_size = 50
# chunk = report_file.read(chunk_size)
# chunk1 = report_file.read(chunk_size)
# chunk2 = report_file.read(chunk_size)
# chunk3 = report_file.read(chunk_size)
#
# report_file.close()
# print(chunk)
# print()
# print(chunk1)
# print()
# print(chunk2)
# print()
# print(chunk3)
#
#


chunk_size = 50
chunk = report_file.read(chunk_size)

while chunk:
    print(chunk)
    print("*" * 50)
    chunk = report_file.read(chunk_size)

report_file.close()


