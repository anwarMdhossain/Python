import python_mysql_dbconfig
from mysql.connector import MySQLConnection,Error

def find_all_book_details():
    try:
        connector=python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        conn=MySQLConnection(**connector)
        if conn.is_connected():
            print("COnnection to MySQL is successful!!")
            cursor=conn.cursor()
            cursor.callproc("find_all_book_author")
            for details in cursor.stored_results():
                #print(details.fetchone())
                #print(details.fetchmany(5))
                print(details.fetchall())
        else:
            print("Connection to MySQL is not established")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def find_book_by_isbn(arg):
    try:
        connector=python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        conn=MySQLConnection(**connector)
        if conn.is_connected():
            print("COnnection to MySQL is successful!!")
            cursor=conn.cursor()
            args=[arg,0]
            result=cursor.callproc("findWithisbn",args)
            print("Title of the ook is:",result[1])
        else:
            print("Connection to MySQL is not established")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    #find_all_book_details()
    arg='1232423190947'
    find_book_by_isbn(arg)