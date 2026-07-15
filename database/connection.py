import mysql.connector
from config import DB_CONFIG

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            return connection,cursor
            
    except mysql.connector.Error as e:
        print(f"Database Error : {e}")
        return None , None
    
def close_connection(connection , cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()