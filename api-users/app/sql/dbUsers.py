from mysql.connector import connect, Error
import os
from app.sql.dbCountries import oneCountry
import datetime

def addUser(myvalue):
    try:
        with connect(
            unix_socket="/var/run/mysqld/mysql.sock",
            user="root",
            password="root11",
            database="list_users"
        ) as connection:
            parmesano = """
            INSERT INTO users (first_name, last_name, birthday, country_code) VALUES (%s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                if (oneCountry(myvalue['country']) == "Data not found"):
                    return "Agrega Pais"
                country_id = oneCountry(myvalue['country'])[0]
                #Query add user table
                cursor.execute(parmesano,(myvalue["first_name"], myvalue["last_name"], myvalue["birthday"], country_id,))
                connection.commit()
                return "Country Added" 
    except Error as e:
        print(e)
        return "Error"

def allUsers():
    try:
        with connect(
            unix_socket="/code/schemas2/sockets/mysqld.sock",
            user="root",
            password="root11",
            database="list_users"
        ) as connection:
            insert_countries_table_query = """
            SELECT * FROM users
            """
            with connection.cursor() as cursor:
                #Query alter countries table
                cursor.execute(insert_countries_table_query)
                result = cursor.fetchall()
                users=[]
                for i in result:
                    myid, first_name, last_name, birthday, country_code = i
                    users.append([myid,first_name,last_name,str(birthday),country_code])
                return users
    except Error as e:
        print(e)
        return "Error"