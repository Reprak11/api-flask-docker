from getpass import getpass
from mysql.connector import connect, Error
import os

def allCountries():
    try:
        with connect(
            host="localhost",
            user="root",
            password=os.getenv('password'),
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
                return result
    except Error as e:
        print(e)
        return "Error"