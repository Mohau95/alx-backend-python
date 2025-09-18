#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 1-execute.py

Reusable context manager to execute a query with parameters.
"""

import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None, db_name='users.db'):
        self.query = query
        self.params = params or ()
        self.db_name = db_name
        self.conn = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with ExecuteQuery(query, params) as results:
        print(results)
