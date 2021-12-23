import pyodbc
import pymssql

class Connection:

    def __init__(self, driver, server, database, username, password, conn_type):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_type = conn_type

    def db_connect_pydbc(self):
        return pyodbc.connect(
            'DRIVER={' + self.driver + '};SERVER=' + self.server + ';DATABASE=' + self.database +
            ';UID=' + self.username + ';PWD=' + self.password + ';Trusted_connection=' + self.conn_type)

    def db_connect_pymssql(host, user, password, database):
        conn = pymssql.connect(host=host, user=user, password=password, database=database)
        return conn
