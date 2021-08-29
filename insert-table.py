from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
        database="list_users"
    ) as connection:
        insert_countries_table_query = """
        INSERT INTO countries (name) VALUES (%s)
        """
        countries_list = [
            ('Argentina',),
            ('Brazil',),
            ('Colombia',),
            ('Peru',),
            ('Bolivia',),
            ('Ecuador',),
            ('Venezuela',),
            ('Guatemala',),
            ('Costa Rica',),
            ('España',),
        ]
        with connection.cursor() as cursor:
            #Query alter countries table
            cursor.executemany(insert_countries_table_query, countries_list)
            connection.commit()

except Error as e:
    print(e)