"""Восстанавливает отдельную учебную базу клиентов из SQL.
Запуск: python prepare_database.py
"""
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
SQL_FILE = BASE / 'data' / 'clients_seed.sql'
DATABASE_FILE = BASE / 'data' / 'clients.db'
if not SQL_FILE.is_file():
    raise FileNotFoundError(SQL_FILE)
with sqlite3.connect(DATABASE_FILE) as connection:
    connection.executescript(SQL_FILE.read_text(encoding='utf-8'))
    total = connection.execute('SELECT COUNT(*) FROM clients').fetchone()[0]
print(f'База {DATABASE_FILE} готова. Клиентов: {total}')
