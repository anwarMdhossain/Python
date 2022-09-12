import python_mysql_dbconfig
from mysql.connector import MySQLConnection,Error

def read_file(file_pic):
    with open(file_pic,"rb") as f:
        pic=f.read()
    return pic

def write_pic(pic):
    with open("D:\Python_projects\Python_practice\photo4.jpg","wb") as file:
        file.write(pic)

def update_blob_data(author_id,pic_path):
    try:
        connector=python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        conn=MySQLConnection(**connector)
        if conn.is_connected():
            print("COnnection to MySQL is successful!!")
            cursor=conn.cursor()
            data=read_file(pic_path)
            query="update authors " \
                  "set photo=%s" \
                  "where id=%s"
            args=(data,author_id)
            cursor.execute(query,args)
            print("Number of rows updated:",cursor.rowcount)
            conn.commit()
            #cursor.execute(commit)
        else:
            print("Connection to MySQL is not established")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def fetch_blob_data(author_id):
    try:
        connector=python_mysql_dbconfig.mysql_db_config(filename="config.ini",section="mysql")
        conn=MySQLConnection(**connector)
        if conn.is_connected():
            print("COnnection to MySQL is successful!!")
            cursor=conn.cursor()
            query="select photo from authors where id=%s"
            args=author_id,
            cursor.execute(query,args)
            data=cursor.fetchone()[0]
            write_pic(data)
            print("Number of rows fetched:",cursor.rowcount)
        else:
            print("Connection to MySQL is not established")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__=="__main__":
    #update_blob_data(43,"D:\Python_projects\Python_practice\photo3.jpg")
    fetch_blob_data(44)