import python_mysql_dbconfig
from mysql.connector import MySQLConnection,Error

def iter_rows(cursor,size=5):
    while True:
        rows=cursor.fetchmany(size)
        if not rows:
            break
        else:
            for row in rows:
                yield row

def query_with_fetchone():
    list1=[]
    try:
        connection_var_dict = python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        connector=MySQLConnection(**connection_var_dict)
        cursor=connector.cursor()
        cursor.execute("select first_name,last_name from authors")
        #for single row fectch
        '''row=cursor.fetchone()
        while row is not None:
            list1.append(row)
            row=cursor.fetchone()'''
        # for all rows fectch
        '''rows=cursor.fetchall()
        print("Total number of records present:",cursor.rowcount)
        for row in rows:
            list1.append(row)'''
        #for fetching multiple records at a time
        for row in iter_rows(cursor,2):
            list1.append(row)

        print("Total number of records present:", cursor.rowcount)
        print(list1)

    except Error as e:
        print(e)
    finally:
        if connector.is_connected():
            cursor.close()
            connector.close()

def insert_new_books(args):
    try:
        connection_var_dict = python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        connector=MySQLConnection(**connection_var_dict)
        cursor=connector.cursor()
        query="INSERT ignore INTO books(title,isbn)"\
            "VALUES(%s,%s)"
        #cursor.execute("INSERT ignore INTO books(title,isbn) VALUES('A Sudden Light','9781439187036')")
        #cursor.execute(query,args)
        cursor.executemany(query, args)
        connector.commit()
        print("Last inserted rowid:",cursor.lastrowid)
    except Error as e:
        print(e)

if __name__=="__main__":
    #query_with_fetchone()
    args = [('Gone with the Window', '9780446675546'),
           ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
    insert_new_books(args)


