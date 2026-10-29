from pathlib import Path
from docxtpl import DocxTemplate
from datetime import date

from emplyees_data import load_employees, find_contact_issues


BASE_DIR = Path(__file__).resolve().parent

HR_TEMPLATE_FILE = BASE_DIR / 'templates' / 'hr_report.docx'
HR_OUTPUT_FILE = BASE_DIR / 'output' / 'HR_отчет.docx'


def prepare_hr_report(employees: list[dict], issues: list[dict]) -> dict:

    departments_by_name = {}

    for employee in employees:
        name = employee.get("department")

        if name not in departments_by_name:
            departments_by_name[name] = {
                "name": name,
                "count": 0,
                "salary_total": 0,
            }

        departments_by_name[name]["count"] += 1
        departments_by_name[name]["salary_total"] += employee["salary"]

    departments = []
    for name in sorted(departments_by_name):
        stats = departments_by_name[name]
        departments.append({
            "name": stats["name"],
            "count": stats["count"],
            "salary_total": f'{stats["salary_total"]} ₽'
        })

    invalid_codes = {issue["code"] for issue in issues}

    prepared_employees = []
    for employee in employees:
        prepared = employee.copy()
        prepared["salary_display"] = f'{employee["salary"]} ₽'
        prepared["quality"] = "Ошибка" if employee["employee_code"] in invalid_codes else "ОК"
        prepared_employees.append(prepared)

    total_payroll = sum(employee["salary"] for employee in employees)

    context = {
        "company_name": "ООО <Рога и Копыта>",
        "report_date": date.today().strftime("%d.%m.%Y"),
        "employees": prepared_employees,
        "total_employees": len(employees),
        "total_departments": len(departments),
        "total_payroll": f'{total_payroll} ₽',
        "problem_count": len(issues),
        "departments": departments,
        "issues": issues,

    }

    return context


def create_hr_report(employees: list[dict], issues: list[dict]) -> Path:
    if not employees:
        raise ValueError("Невозможно создать отчет - список пуст")

    if not HR_TEMPLATE_FILE.is_file():
        raise FileNotFoundError(f"file not found at {HR_TEMPLATE_FILE}")

    context = prepare_hr_report(employees, issues)

    doc = DocxTemplate(HR_TEMPLATE_FILE)

    print(f"Шаблон загружен {HR_TEMPLATE_FILE.name}")

    missing_variables = doc.get_undeclared_template_variables(context=context)

    if missing_variables:
        raise ValueError(f"Есть не переданные данные {missing_variables}")

    doc.render(context, autoescape=True)
    HR_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    doc.save(HR_OUTPUT_FILE)

    return HR_OUTPUT_FILE


if __name__ == '__main__':
    employees = load_employees()
    issues = find_contact_issues(employees)

    report_file = create_hr_report(employees, issues)

    print(f'Сотрудников выгружено: {len(employees)}')
    print(f'Ошибок обнаружено: {len(issues)}')
    print(f'Файл сохранен: {report_file}')
