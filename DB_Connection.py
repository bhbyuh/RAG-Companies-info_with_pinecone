import psycopg2

def session_making(DB_password,database_name):
    conn = psycopg2.connect(
        dbname=database_name,
        user="postgres",
        password=DB_password,
        host="localhost",
        port=5432
    )

    cur = conn.cursor()

    return [conn,cur]