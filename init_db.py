import sqlite3

# This automatically creates an 'ai_eval.db' file in your project folder
connection = sqlite3.connect("ai_eval.db")
cursor = connection.cursor()

# Create the exact same evaluation logging table structure
cursor.execute("""
CREATE TABLE IF NOT EXISTS evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    expected_answer TEXT,
    actual_answer TEXT,
    score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()
print("Success! SQLite local database and evaluations table initialized.")