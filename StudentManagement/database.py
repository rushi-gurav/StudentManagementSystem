import sqlite3

def setup_db():
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        sub_mark1 INTEGER NOT NULL,
        sub_mark2 INTEGER NOT NULL,
        sub_mark3 INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()