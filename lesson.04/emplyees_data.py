import sqlite3
from pathlib import Path

from validators import is_valid_employee_code, is_valid_phone, is_valid_email


BASE_DIR = Path(__file__).resolve().parent

DATABASE_FILE = BASE_DIR / 'data' / 'employees.db'


def load_employees():
    """..."""
    if not DATABASE_FILE.is_file():
        raise FileNotFoundError(f"Database file not found at {DATABASE_FILE}")

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    try:

        rows = connection.execute(
            """SELECT *  FROM employees ORDER BY id;  """
        )
        employees = [dict(row) for row in rows]
        return employees

    finally:
        connection.close()


def find_contact_issues(employees: list[dict]) -> list[dict]:
    """..."""
    issues = []

    fields_to_check = (
        ("Email", "email", is_valid_email),
        ("Телефон", "phone", is_valid_phone),
        ("Код сотрудника", "employee_code", is_valid_employee_code),
    )

    for employee in employees:
        for label, key, validator in fields_to_check:
            if not validator(employee[key]):
                issues.append(
                    {
                        "code": employee["employee_code"],
                        "employee": employee["full_name"],
                        "field": label,
                        "value": employee[key],
                    }
                )
    return issues


if __name__ == '__main__':
    users = load_employees()
    print(users[:5])

    result_issues = find_contact_issues(users)
    print(result_issues)

