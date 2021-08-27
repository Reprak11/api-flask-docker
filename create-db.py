from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: ")
    ) as connection:
        print(connection)
        create_db_query = "CREATE DATABASE list_users"
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)