import sqlite3

conn = sqlite3.connect("/app/db/std.db")
sql = """Create table students(
        id int,
        name text,
        gender text)"""
conn.execute(sql)
conn.close()