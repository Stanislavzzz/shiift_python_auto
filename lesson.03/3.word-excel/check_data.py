"""Простая проверка подготовленной базы SQLite.
"""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "data" / "employees.db"


def show_database_summary():

    if not DATABASE_FILE.is_file():
        print("База отсутствует. Сначала выполните python prepare_database.py")
        return

    connection.row_factory = sqlite3.Row

    try:

        total = connection.execute("SELECT COUNT(*) AS total FROM employees").fetchone()
        departments = connection.execute(
            "SELECT COUNT(DISTINCT department) AS total FROM employees"
        ).fetchone()
        salary = connection.execute(
            "SELECT SUM(salary) AS total FROM employees"
        ).fetchone()
        preview = connection.execute(
            "SELECT employee_code, full_name, department, salary "
            "FROM employees ORDER BY id LIMIT 5"
        ).fetchall()

        print(f"Записей: {total['total']}")
        print(f"Отделов: {departments['total']}")
        print(f"Фонд окладов: {salary['total']:,} ₽".replace(",", " "))
        print("Первые пять сотрудников:")
        for row in preview:
            print(f"  {row['employee_code']} | {row['full_name']} | "
                  f"{row['department']} | {row['salary']:,} ₽".replace(",", " "))
    finally:

        connection.close()


if __name__ == "__main__":
    show_database_summary()
