#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 0-databaseconnection.py

Class-based context manager for opening/closing database connections.
"""

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)
