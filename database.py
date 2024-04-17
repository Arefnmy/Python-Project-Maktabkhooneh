import mysql.connector


class Database:
    DATABASE_NAME = 'python_project'
    TABLE_NAME = 'car_used'

    def __init__(self):
        self.cnx = None
        self.cursor = None

    def connect_to_database(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database=Database.DATABASE_NAME)
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)

    def close(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
