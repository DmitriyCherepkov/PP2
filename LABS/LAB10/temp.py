import psycopg2

host = "localhost"
port = "5432"
dbname = "snake"
user = "postgres"
password = "1"

try:
    with psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    ) as connection:
        with connection.cursor() as cursor:
            # SQL statement as a string
            create_table_query = """
            CREATE TABLE IF NOT EXISTS scores (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                score INTEGER NOT NULL
            );
            """
            cursor.execute(create_table_query)
            connection.commit()  # Commit the transaction
            print("Table created successfully.")

except psycopg2.Error as error:
    print(f"Database error: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")