"""Создание учебной SQLite-базы из SQL-скрипта.

Запуск из корня проекта: python prepare_database.py
"""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

SQL_SCRIPT = BASE_DIR / "data" / "employees_seed.sql"
DATABASE_FILE = BASE_DIR / "data" / "employees.db"


def prepare_database():
    """Создаёт/пересоздаёт учебную таблицу employees из SQL-файла."""

    if not SQL_SCRIPT.is_file():
        raise FileNotFoundError(f"Не найден SQL-скрипт: {SQL_SCRIPT}")

    sql_commands = SQL_SCRIPT.read_text(encoding="utf-8")
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)


    with sqlite3.connect(DATABASE_FILE) as connection:

        connection.executescript(sql_commands)

        count = connection.execute("SELECT COUNT(*) FROM employees").fetchone()[0]

    print(f"База готова: {DATABASE_FILE}")
    print(f"Сотрудников: {count}")


if __name__ == "__main__":
    prepare_database()
