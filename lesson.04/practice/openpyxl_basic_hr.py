from pathlib import Path
from openpyxl import load_workbook, Workbook


BASE_DIR = Path(__file__).resolve().parents[1]

TEMPLATE_FILE = BASE_DIR / 'templates' / 'hr_report.xlsx'

if not TEMPLATE_FILE.is_file():
    raise FileNotFoundError(f"file not found at {TEMPLATE_FILE}")


template_book = load_workbook(TEMPLATE_FILE)
print(f"Листы книги: {template_book.sheetnames}")
template_sheet = template_book["Сотрудники"]

print(f'Столбец B8: {template_sheet["B8"].value}')
print(f'Ячейка для кода B9: {template_sheet["B9"].value}')
print(f'Последняя строка: {template_sheet.max_row}')


print(f'Формула ячейки: {template_sheet["A6"].value}')

template_book.close()

# sheet = workbook.active
# sheet.title = "Сотрудники"
# print(f"Листы книги: {workbook.sheetnames}")
#
#
# sheet["A1"] = "Код"
# sheet["B1"] = "ФИО"
# sheet["C1"] = "ОКЛАД"
#
# print(f'Заголовок A1: {sheet["A1"].value}')
#
#
# sheet.cell(row=2, column=1, value="ЕМР-0001")
# sheet.cell(row=2, column=2, value="Волков Александр Иванович")
# sheet.cell(row=2, column=3, value="115700")
#
# print(f'Код сотрудника: {sheet["A2"].value}')
# print(f'Оклад сотрудника: {sheet.cell(row=2, column=3).value}')
#
# print()
# print()
#
#
# sheet.append(["EMP-0002", "Макарова Ксения Дмитриевна", 97000])
# sheet.append(["EMP-0003", "Соловьёв Тимофей Михайлович", 125400])
# sheet.append(["EMP-0004", "Новикова Ольга Алексеевна", 35400])
#
# print(f'Третий сотрудник: {sheet["B4"].value}')
# print(f'Последняя строка: {sheet.max_row}')
#
# print()
# print()
#
# notes_sheet = workbook.create_sheet("Примечания")
# notes_sheet["A1"] = "Тестовая книга"
#
# employees_sheet = workbook["Сотрудники"]
#
# print(f"Все Листы книги: {workbook.sheetnames}")
#
#
# ##########################
#
# OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
#
# workbook.save(OUTPUT_FILE)
# workbook.close()
#
