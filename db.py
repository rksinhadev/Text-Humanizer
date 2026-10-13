
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="text_humanizer"
    )

if __name__ == "__main__":
    try:
        connection = get_connection()
        print("MySQL connected successfully!")

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        print("Database:", cursor.fetchone()[0])

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
