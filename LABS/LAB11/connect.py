import psycopg2
import csv

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "phonebook",
    "user": "postgres",
    "password": "1"
}

def connect_to_db():
    return psycopg2.connect(**DB_CONFIG)

def validate_phone_number(phone_number):
    return phone_number.isdigit()

def record_exists(cursor, query, value):
    cursor.execute(query, (value,))
    return cursor.fetchone()[0] > 0

def insert_or_update_user(cursor, connection):
    name = input("Your name: ").strip()
    phone_number = input("Your phone number: ").strip()

    if not all([name, phone_number]):
        print("Name and phone number are required.")
        return

    if not validate_phone_number(phone_number):
        print("Invalid phone number. It should contain only digits.")
        return

    cursor.execute("SELECT id FROM people WHERE name = %s", (name,))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE people SET phone_number = %s WHERE id = %s", (phone_number, user[0]))
        print("Phone number updated for existing user.")
    else:
        surname = input("Your surname: ").strip()
        if not surname:
            print("Surname is required for new users.")
            return
        cursor.execute("INSERT INTO people (name, surname, phone_number) VALUES (%s, %s, %s)", (name, surname, phone_number))
        print("New user added.")

    connection.commit()

def update_user_info(cursor, connection):
    user_id = input("Enter id: ").strip()
    if not user_id.isdigit():
        print("Invalid ID.")
        return

    cursor.execute("SELECT * FROM people WHERE id = %s", (user_id,))
    row = cursor.fetchone()

    if not row:
        print(f"The id {user_id} doesn't exist.")
        return

    print("Current info:", row)
    new_name = input("New name: ").strip()
    new_surname = input("New surname: ").strip()
    new_phone_number = input("New phone number: ").strip()

    cursor.execute("""
        UPDATE people
        SET name = %s, surname = %s, phone_number = %s
        WHERE id = %s
    """, (new_name, new_surname, new_phone_number, user_id))
    connection.commit()
    print("Data updated successfully!")

def find_people_by_phone_number(cursor):
    num = input("Enter starting digits of phone number: ").strip()
    cursor.execute("SELECT * FROM people WHERE phone_number LIKE %s ORDER BY name ASC", (num + '%',))
    for row in cursor.fetchall():
        print(row)

def find_people_by_name(cursor):
    name = input("Enter the name: ").strip()
    cursor.execute("SELECT * FROM people WHERE name LIKE %s ORDER BY name ASC", (name + '%',))
    for row in cursor.fetchall():
        print(row)

def find_people_by_surname(cursor):
    surname = input("Enter the surname: ").strip()
    cursor.execute("SELECT * FROM people WHERE surname LIKE %s ORDER BY name ASC", (surname + '%',))
    for row in cursor.fetchall():
        print(row)

def delete_user(cursor, connection):
    option = input("1 - Delete by name | 2 - Delete by phone number: ")
    field = "name" if option == "1" else "phone_number" if option == "2" else None

    if not field:
        print("Invalid option.")
        return

    value = input(f"Enter the {field.replace('_', ' ')}: ").strip()

    if not record_exists(cursor, f"SELECT COUNT(*) FROM people WHERE {field} = %s", value):
        print(f"No records found with the {field.replace('_', ' ')} '{value}'.")
        return

    cursor.execute(f"DELETE FROM people WHERE {field} = %s", (value,))
    connection.commit()
    print("Record(s) deleted successfully!")

def query_with_pagination(cursor):
    try:
        limit = int(input("Enter limit (number of records per page): "))
        offset = int(input("Enter offset (starting point): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    cursor.execute("SELECT * FROM people ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found for the given limit and offset.")

def import_from_csv(cursor, connection):
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, surname, phone_number = map(str.strip, row[:3])

            if not validate_phone_number(phone_number):
                print(f"Invalid phone number: {phone_number}")
                continue

            cursor.execute("""
                SELECT COUNT(*) FROM people
                WHERE name = %s OR surname = %s OR phone_number = %s
            """, (name, surname, phone_number))

            if cursor.fetchone()[0] > 0:
                print(f"Duplicate found: {name} {surname} {phone_number}")
                continue

            cursor.execute("INSERT INTO people (name, surname, phone_number) VALUES (%s, %s, %s)", (name, surname, phone_number))
            connection.commit()
            print(f"User {name} {surname} added successfully.")

def main():
    try:
        with connect_to_db() as connection:
            with connection.cursor() as cursor:
                while True:
                    choice = input("\n1 - Add new user\n2 - Update user\n3 - Find by phone\n4 - Delete user\n5 - Import from CSV\n6 - Find by phone\n7 - Exit\nChoose an option: ")

                    options = {
                        "1": lambda: insert_or_update_user(cursor, connection),
                        "2": lambda: update_user_info(cursor, connection),
                        "3": lambda: find_people_by_phone_number(cursor),
                        "4": lambda: find_people_by_name(cursor),
                        "5": lambda: find_people_by_surname(cursor),
                        "6": lambda: delete_user(cursor, connection),
                        "7": lambda: import_from_csv(cursor, connection),
                        "8": lambda: query_with_pagination(cursor),
                        "9": lambda: exit()
                    }

                    action = options.get(choice)
                    if action:
                        action()
                    else:
                        print("Invalid option. Try again.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()