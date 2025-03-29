from fastapi import FastAPI, Depends, HTTPException
import sqlite3
import os

app = FastAPI()

DATABASE = os.getenv("DB_PATH", "/data/fruits.db")
DB_HOST = os.getenv("DB_HOST", "localhost")

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/stock")
def read_stock(limit: int = 10):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock ORDER BY id LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/stock/{fruit_name}")
def fruit_stock(fruit_name: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock WHERE fruit=?", (fruit_name,))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return [dict(row) for row in rows]
