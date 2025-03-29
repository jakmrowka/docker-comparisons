import sqlite3
import random
from faker import Faker
import os

fake = Faker()

if not os.path.exists("/data/fruits.db"):
    conn = sqlite3.connect("/data/fruits.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fruit TEXT,
            quantity INTEGER,
            last_updated TEXT
        )
    """)

    fruits = ['apple', 'banana', 'orange', 'kiwi', 'pineapple', 'grape', 'mango', 'strawberry', 'peach', 'pear']

    for _ in range(100):
        fruit = random.choice(fruits)
        quantity = random.randint(1, 100)
        last_updated = fake.iso8601()
        cursor.execute("INSERT INTO stock (fruit, quantity, last_updated) VALUES (?, ?, ?)",
                       (fruit, quantity, last_updated))

    conn.commit()
    conn.close()
