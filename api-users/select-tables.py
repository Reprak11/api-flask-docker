from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        unix_socket="/var/run/mysqld/mysql.sock",
        user="root",
        password="root11"
        database="list_users"
    ) as connection:
        insert_countries_table_query = """
        SELECT * FROM countries
        """
        with connection.cursor() as cursor:
            #Query alter countries table
            cursor.execute(insert_countries_table_query)
            result = cursor.fetchall()
            [print(row) for row in result] 

except Error as e:
    print(e)