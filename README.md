#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 0-databaseconnection.py

Class-based context manager for handling database connections.
"""

import sqlite3


class DatabaseConnection:
    """Custom context manager to handle opening and closing DB connections."""

    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)
#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 1-execute.py

Reusable context manager to execute a query with parameters.
"""

import sqlite3


class ExecuteQuery:
    """Executes a query within a context manager."""

    def __init__(self, query, params=(), db_name="users.db"):
        self.query = query
        self.params = params
        self.db_name = db_name
        self.conn = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(query, (25,)) as results:
        print(results)
#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 3-concurrent.py

Concurrent asynchronous database queries using aiosqlite.
"""

import asyncio
import aiosqlite


async def async_fetch_users():
    """Fetch all users from DB asynchronously."""
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        return rows


async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        return rows


async def fetch_concurrently():
    """Run both queries concurrently."""
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(),
    )
    print("All Users:", results[0])
    print("Users older than 40:", results[1])


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
