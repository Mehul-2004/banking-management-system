import mysql.connector
from config import DB_CONFIG

def get_connection():
    """
    Create and return a MySQL database connection and cursor.

    Returns :
        tuple: (connection, cursor) 
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor

    except mysql.connector.Error as e:
        print(f"Database Error : {e}")
        return None, None
    
def close_connection(connection, cursor):
    """
    Safely close the database connection and cursor.
    """
    if cursor:
        cursor.close()
    if connection:
        connection.close()