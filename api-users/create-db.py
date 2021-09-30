from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        unix_socket="/var/run/mysqld/mysql.sock",
        user="root",
        password="root11"
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