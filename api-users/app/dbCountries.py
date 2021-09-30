from mysql.connector import connect, Error
import os

def allCountries():
    try:
        with connect(
            unix_socket="/code/schemas2/sockets/mysqld.sock",
            user="root",
            password="root11",
            database="list_users"
        ) as connection:
            insert_countries_table_query = """
            SELECT * FROM countries
            """
            with connection.cursor() as cursor:
                #Query alter countries table
                cursor.execute(insert_countries_table_query)
                result = cursor.fetchall()
                return result
    except Error as e:
        return "Error"

def oneCountry(myvalue):
    try:
        with connect(
            unix_socket="/code/schemas2/sockets/mysqld.sock",
            user="root",
            password="root11",
            database="list_users"
        ) as connection:
            get_countries_table_value_int_query = """
            SELECT name FROM countries WHERE code=(%s)
            """
            get_countries_table_value_string_query = """
            SELECT code FROM countries WHERE name=(%s)
            """
            with connection.cursor() as cursor:
                #Query alter countries table
                cursor.execute(get_countries_table_value_int_query,(myvalue,)) if type(myvalue) is int else cursor.execute(get_countries_table_value_string_query,(myvalue,))
                result = cursor.fetchall()
                return "Data not found" if result==[] else result[0]
    except Error as e:
        print(e)
        return "Error"

def addCountry(myvalue):
    try:
        with connect(
            unix_socket="/code/schemas2/sockets/mysqld.sock",
            user="root",
            password="root11",
            database="list_users"
        ) as connection:
            parmesano = """
            INSERT INTO countries (name) VALUES (%s)
            """
            with connection.cursor() as cursor:
                if (oneCountry(myvalue) != "Data not found"):
                    return "Country already in list"
                #Query alter countries table
                cursor.execute(parmesano,(myvalue,))
                connection.commit()
                return "Country Added" 
    except Error as e:
        print(e)
        return "Error"