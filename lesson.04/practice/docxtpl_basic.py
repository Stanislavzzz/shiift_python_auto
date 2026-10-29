from pathlib import Path
from docxtpl import DocxTemplate


BASE_DIR = Path(__file__).resolve().parents[1]

TEMPLATE_FILE = BASE_DIR / 'templates' / 'employee_card.docx'
OUTPUT_FILE = BASE_DIR / 'output' / 'TEST_card.docx'

if not TEMPLATE_FILE.is_file():
    raise FileNotFoundError(f"file not found at {TEMPLATE_FILE}")

doc = DocxTemplate(TEMPLATE_FILE)

print(f"Шаблон загружен {TEMPLATE_FILE.name}")

context = {
    # ""
    "employee_name": "Волков Андрей Сергеевич",
    "position": "Python-разработчик",
    "salary": "114000 руб",
    "report_data": "29.10.2026"
}

missing_variables = doc.get_undeclared_template_variables(context=context)
print(missing_variables)

# 1,EMP-0001,Волков Андрей Сергеевич,Разработка ПО,Python-разработчик,114000,andrey.volkov.001@example.org,+7 (901) 201-01-07,2016-02-17

# if __name__ == '__main__':
#     employees = load_employees()
#     issues = find_contact_issues(employees)
#
#     result = create_excel_report(employees, issues)

    #
    # print(f'Сотрудников выгружено: {len(employees)}')
    # print(f'Ошибок обнаружено: {len(issues)}')
    # print(f'Файл сохранен: {result}')
    #


