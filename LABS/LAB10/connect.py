import psycopg2
import csv

host = "localhost"
port = "5432"
dbname = "phonebook"
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
            choice = input("1 - Add new user | 2 - Change existing information | 3 - Withdraw all people | 4 - Delete: ")
            
            if choice == "1":
                name = input("Your name: ").strip()
                surname = input("Your surname: ").strip()
                phone_number = input("Your phone number: ").strip()
                
                cursor.execute("""
                    SELECT COUNT(*)
                    FROM people
                    WHERE name = %s OR surname = %s OR phone_number = %s
                """, (name, surname, phone_number))

                count = cursor.fetchone()[0]

                if count > 0:
                    print("A person with the same name, surname, or phone number already exists.")
                else:
                    if not phone_number.isdigit():
                        print("Invalid phone number. It should contain only digits.")
                    else:
                        cursor.execute("""
                            INSERT INTO people (name, surname, phone_number)
                            VALUES (%s, %s, %s)
                        """, (name, surname, phone_number))

                        connection.commit()
                        print("User added successfully.")
            
            elif choice == "2":
                user_id = int(input("Enter id: "))

                # Check if the id exists first
                cursor.execute("SELECT COUNT(*) FROM people WHERE id = %s", (user_id,))
                count = cursor.fetchone()[0]

                if count > 0:
                    # If the id exists, fetch the rows and display them
                    cursor.execute("SELECT * FROM people WHERE id = %s", (user_id,))
                    rows = cursor.fetchall()

                    for row in rows:
                        print(row)

                    # Proceed with updating the data
                    new_name = input("New name: ")
                    new_surname = input("New surname: ")
                    new_phone_number = input("New phone number: ")

                    cursor.execute("""
                        UPDATE people
                        SET name = %s, surname = %s, phone_number = %s
                        WHERE id = %s
                    """, (new_name, new_surname, new_phone_number, user_id))          
                    connection.commit()

                    print("Data updated successfully!")
                else:
                    print(f"The id {user_id} doesn't exist.")
            
            elif choice == "3":
                num = input("How do you want to query your table? ")
                cursor.execute(f"SELECT * FROM people WHERE phone_number LIKE '{num}%' ORDER BY name ASC")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            
            elif choice == "4":
                option = input("1 - Delete by name | 2 - Delete by phone number: ")
                
                if option == "1":
                    name = input("Enter the name of the record to delete: ")
                    
                    # Check if the record with the given name exists
                    cursor.execute("SELECT COUNT(*) FROM people WHERE name = %s", (name,))
                    count = cursor.fetchone()[0]
                    
                    if count > 0:
                        cursor.execute("DELETE FROM people WHERE name = %s", (name,))
                        connection.commit()
                        print(f"Record(s) with name '{name}' deleted successfully!")
                    else:
                        print(f"No records found with the name '{name}'.")

                elif option == "2":
                    phone_number = input("Enter the phone number of the record to delete: ")
                    
                    # Check if the record with the given phone number exists
                    cursor.execute("SELECT COUNT(*) FROM people WHERE phone_number = %s", (phone_number,))
                    count = cursor.fetchone()[0]
                    
                    if count > 0:
                        cursor.execute("DELETE FROM people WHERE phone_number = %s", (phone_number,))
                        connection.commit()
                        print(f"Record(s) with phone number '{phone_number}' deleted successfully!")
                    else:
                        print(f"No records found with the phone number '{phone_number}'.")
            
            elif choice == "5":
                # Open the CSV file
                with open('data.csv', mode='r', newline='') as file:
                    reader = csv.reader(file)

                    # Iterate over each row in the CSV file
                    for row in reader:
                        name = row[0].strip()
                        surname = row[1].strip()
                        phone_number = row[2].strip()

                        # Check if the person already exists in the database
                        cursor.execute("""
                            SELECT COUNT(*)
                            FROM people
                            WHERE name = %s OR surname = %s OR phone_number = %s
                        """, (name, surname, phone_number))

                        count = cursor.fetchone()[0]

                        # If a person already exists, don't add them
                        if count > 0:
                            print(f"A person with the same name, surname, or phone number already exists: {name} {surname} {phone_number}")
                        else:
                            if not phone_number.isdigit():
                                print(f"Invalid phone number. It should contain only digits: {phone_number}")
                            else:
                                cursor.execute("""
                                    INSERT INTO people (name, surname, phone_number)
                                    VALUES (%s, %s, %s)
                                """, (name, surname, phone_number))

                                # Commit after each successful insert
                                connection.commit()
                                print(f"User {name} {surname} added successfully.")
                                
except psycopg2.Error as error:
    print(f"Database error: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")