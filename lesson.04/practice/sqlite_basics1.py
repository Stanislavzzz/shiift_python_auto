import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


DATABASE_FILE = BASE_DIR / 'data' / 'employees.db'

if not DATABASE_FILE.is_file():
    raise FileNotFoundError(f"Database file not found at {DATABASE_FILE}")

print(f"База найдена: {DATABASE_FILE}")

connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.execute(
    "SELECT id, full_name, salary FROM employees"
)

first_employee = cursor.fetchone()
if first_employee:
    print(first_employee[0])
    print(first_employee[1])
    print(first_employee[2])
    # print(first_employee)
    # print(type(first_employee))

connection.close()