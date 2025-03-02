import mysql.connector
from mysql.connector import Error

hostname = "e8ls6.h.filess.io"
database = "olistproject_planetwell"
port = 3307
username = "olistproject_planetwell"
password = "f44220d2c2631e317c3565fc5939b76a1781d080"

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")