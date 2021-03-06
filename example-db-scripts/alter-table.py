from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
        database="list_users"
    ) as connection:
        alter_countries_table_query = """
        ALTER TABLE countries
        MODIFY COLUMN name VARCHAR(50)
        """
        show_countries_table_query = "DESCRIBE countries"
        with connection.cursor() as cursor:
            #Query alter countries table
            cursor.execute(alter_countries_table_query)
            #Query countries table
            cursor.execute(show_countries_table_query)
            result = cursor.fetchall()
            [print(row) for row in result]

except Error as e:
    print(e)