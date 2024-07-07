
def table_creation(conn,cur):
    cur.execute("""
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema='public'
        AND table_name='companies'
    );
    """)

    table_exists=cur.fetchone()[0]

    if(not table_exists):
        cur.execute("""
            Create table companies(
            CR_number SERIAL PRIMARY KEY,
            company_name VARCHAR(20),
            email VARCHAR(20)
            )
            """)
        print("Table created successfully")
    
    conn.commit()

def company_data_insertion(data,conn,cur):
    cur.execute(f"""
    SELECT * from companies 
    WHERE  CR_number=%s
    """,(data[0],))

    row=cur.fetchall()

    if len(row) == 0:
        cur.execute(f"""
            INSERT INTO companies (CR_number, company_name, email)
            VALUES (%s, %s, %s)
        """, (data[0], data[1], data[2]))
    else:
        return False

    conn.commit()

    return True