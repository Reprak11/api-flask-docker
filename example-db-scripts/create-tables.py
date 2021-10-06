from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
        database="list_users"
    ) as connection:
        create_user_table_query = """
        CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            birthday date,
            country_code INT,
            FOREIGN KEY (country_code) REFERENCES countries(code)
        )
        """
        create_countries_table_query = """
        CREATE TABLE countries(
            code INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            continent VARCHAR(20)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_countries_table_query)
            cursor.execute(create_user_table_query)

except Error as e:
    print(e)