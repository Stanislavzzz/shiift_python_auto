from pathlib import Path
from docxtpl import DocxTemplate
from datetime import date

from emplyees_data import load_employees, find_contact_issues


BASE_DIR = Path(__file__).resolve().parent

TEMPLATE_FILE = BASE_DIR / 'templates' / 'employee_card.docx'
OUTPUT_FILE = BASE_DIR / 'output' / 'Карточка_сотрудник.docx'


def create_employee_card(employee: dict, issues: list[dict]) -> Path:

    if not TEMPLATE_FILE.is_file():
        raise FileNotFoundError(f"file not found at {TEMPLATE_FILE}")

    invalid_codes = {issue["code"] for issue in issues}

    prepared_employee = employee.copy()
    #
    # print(prepared_employee[])
    # print(invalid_codes)

    prepared_employee["salary_display"] = f'{employee["salary"]} ₽'
    #
    prepared_employee["hire_date"] = date.fromisoformat(employee["hire_date"]).strftime("%d.%m.%Y")

    context = {
        "report_date": date.today().strftime("%d.%m.%Y"),
        "employee": prepared_employee,
    }

    doc = DocxTemplate(TEMPLATE_FILE)

    print(f"Шаблон загружен {TEMPLATE_FILE.name}")

    missing_variables = doc.get_undeclared_template_variables(context=context)

    if missing_variables:
        raise ValueError(f"Есть не переданные данные {missing_variables}")

    doc.render(context, autoescape=True)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    doc.save(OUTPUT_FILE)

    return OUTPUT_FILE


if __name__ == '__main__':
    employees = load_employees()
    issues = find_contact_issues(employees)

    result = create_employee_card(employees[0], issues)


    print(f'Сотрудников выгружено: {len(employees)}')
    print(f'Ошибок обнаружено: {len(issues)}')
    print(f'Файл сохранен: {result}')



