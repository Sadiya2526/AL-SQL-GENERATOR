import sqlite3
import os

db_path = r"c:\Users\sksum\OneDrive\Desktop\DA\AI SQL GENERATOR\database.db"

print(f"Database file exists: {os.path.exists(db_path)}")
print(f"Database file size: {os.path.getsize(db_path) if os.path.exists(db_path) else 0} bytes\n")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables in database: {tables}\n")
    
    # If no tables, create one
    if not tables:
        print("No tables found. Creating students table...\n")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        age INTEGER
        )
        """)
        
        data = [
            ("Rahul","Male",21),
            ("Priya","Female",20),
            ("Arjun","Male",22),
            ("Sneha","Female",19),
            ("Kiran","Male",20)
        ]
        
        cursor.executemany(
            "INSERT INTO students(name,gender,age) VALUES(?,?,?)",
            data
        )
        
        conn.commit()
        print("✓ Database created and populated successfully!\n")
    
    # Verify data
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(f"✓ Students in database: {len(students)}")
    for student in students:
        print(f"  {student}")
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
