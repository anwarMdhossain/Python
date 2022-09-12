import python_mysql_dbconfig
import mysql.connector as mysql_connector
from mysql.connector import Error

def mysql_connection():
    db_var=python_mysql_dbconfig.mysql_db_config()
    #print(db_var)
    #connector=mysql_connector.connect(**db_var)
    connector = mysql_connector.CMySQLConnection(**db_var)
    try:
        if connector.is_connected():
            print("Connection Established successfully")
        else:
            print("Connection is not established!!")
    except Error as e:
        print(e)
    finally:
        if connector.is_connected():
            connector.close()
            print("Connection broken successfully")

mysql_connection()