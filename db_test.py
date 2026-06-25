import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="studyplanner",
    user="postgres",
    password="postgres123",
    port="5432"
)

print("Connected successfully!")

conn.close()
