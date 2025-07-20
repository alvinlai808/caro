from flask import Flask, render_template
import os
import time

import psycopg
from psycopg.rows import dict_row

# Database connection settings
DB_HOST = "db"
DB_PORT = 5432
DB_NAME = "caro"
DB_USER = "alvin"
DB_PASSWORD = "923401926"

# Wait for DB to start listening
for _ in range(3):

    conn_str = f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"

    try:
        # Connect to the PostgreSQL server
        with psycopg.connect(conn_str, row_factory=dict_row) as conn:
            print("Connection successful!")

            # Create a cursor and execute a simple query
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
                print("PostgreSQL version:", version["version"])
            
            break

    except Exception as e:
        print("Failed to connect to the database:")
        print(e)

    time.sleep(1)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')