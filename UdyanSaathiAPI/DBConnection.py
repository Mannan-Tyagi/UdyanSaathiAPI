import mysql.connector

class DBConnection:
    @classmethod
    def database_connection(self):
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Impetus@123',
            'database': 'PollutionData'
        }

        try:
            connection = mysql.connector.connect(**db_config)
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None