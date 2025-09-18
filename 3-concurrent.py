#!/usr/bin/env python3
"""
Repo: alx-backend-python
Directory: python-context-async-perations-0x02
File: 3-concurrent.py

Runs multiple asynchronous database queries concurrently using asyncio and aiosqlite.
"""

import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return results

if __name__ == "__main__":
    all_results = asyncio.run(fetch_concurrently())
    print(all_results)
