import psycopg2


def search_records(pattern):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="phonebook",  
            user="postgres",
            password="admin",
            port=5432
        )
        cur = conn.cursor()
        
        query = "SELECT * FROM contacts WHERE first_name ILIKE %s OR second_name ILIKE %s OR CAST(phone AS TEXT) LIKE %s"
        cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return rows
    except Exception as e:
        print("An error occurred:", e)

pattern = input("Enter search pattern: ")
matching_records = search_records(pattern)
if matching_records:
    for record in matching_records:
        print(record)
else:
    print("No matching records found.")
