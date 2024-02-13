import mysql.connector
from mysql.connector import Error
from typing import Optional

def connect_to_mysql(host: str, username: str, password: str, database: str, port: Optional[int] = 3306):
    """
    Connect to MySQL database.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        username (str): The username for accessing the MySQL server.
        password (str): The password for accessing the MySQL server.
        database (str): The name of the database to connect to.
        port (int, optional): The port number of the MySQL server. Defaults to 3306.

    Returns:
        Connection: MySQL connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            port=port
        )
        print("Connected to MySQL Server")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_connection(connection):
    """
    Close the connection to the MySQL database.

    Args:
        connection: MySQL connection object to close.
    """
    if connection:
        connection.close()
        print("MySQL connection closed")

# Example usage:
if __name__ == "__main__":
    host = "localhost"
    username = "your_username"
    password = "your_password"
    database = "your_database_name"
    port = 3306

    connection = connect_to_mysql(host, username, password, database, port)
    if connection:
        # Perform database operations here
        close_connection(connection)
