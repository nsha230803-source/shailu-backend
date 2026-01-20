import os
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="Shailu Backend API")

def get_db_connection():
    return psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host="/cloudsql/" + os.environ["DB_CONNECTION_NAME"],
    )

@app.get("/")
def root():
    return {"message": "Backend running with PostgreSQL"}

@app.get("/db-check")
def db_check():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.close()
    conn.close()
    return {"database": "connected"}

