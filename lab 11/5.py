import psycopg2

def query_with_pagination(limit, offset):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="phonebook", 
            user="postgres",
            password="admin",
            port=5432
        )
        cur = conn.cursor()
        
        query = "SELECT * FROM contacts LIMIT %s OFFSET %s"
        cur.execute(query, (limit, offset))
        
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        # Вывод результатов на экран
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")
        
        return rows
    except Exception as e:
        print("An error has occurred:", e)

# Пример использования функции запроса с пагинацией
limit = 3  # Количество записей на странице
page_number = 1  # Номер страницы (считая с 1)

# Вычисляем смещение (OFFSET) на основе номера страницы
offset = (page_number - 1) * limit

# Запрос с использованием пагинации
query_with_pagination(limit, offset)
