import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="studyplanner",   
            user="postgres",           
            password="postgres123",    
            port="5432"
        )
        return conn

    except Exception as e:
        print("Database Connection Error:", e)
        return None


if __name__ == "__main__":
    conn = get_connection()

    if conn:
        print("✅ Connected successfully to ShaktiDB!")
        conn.close()
    else:
        print("❌ Failed to connect to ShaktiDB.")
