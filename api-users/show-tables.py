from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        unix_socket="/var/run/mysqld/mysql.sock",
        user="root",
        password="root11",
        database="list_users"
    ) as connection:
        show_users_table_query = "DESCRIBE users"
        show_countries_table_query = "DESCRIBE countries"
        with connection.cursor() as cursor:
            #Query users table
            cursor.execute(show_users_table_query)
            result = cursor.fetchall()
            [print(row) for row in result]
            print()
            #Query countries tables
            cursor.execute(show_countries_table_query)
            result = cursor.fetchall()
            [print(row) for row in result]
except Error as e:
    print(e)