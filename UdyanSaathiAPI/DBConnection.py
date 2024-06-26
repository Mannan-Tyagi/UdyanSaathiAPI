import mysql.connector
import os

# class DBConnection:
#     
class DBConnection:
    # keyword = "Azure"
  
    keyword = "Azure"
    if(keyword == "Azure"):
        @classmethod
        def database_connection(self):
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_config = {
                'host': 'mysqlmannan01.mysql.database.azure.com',
                'user': 'mannan',
                'password': 'Khetan@123',
                'database': 'udyaansaathidata',
                'client_flags': [mysql.connector.ClientFlag.SSL],
                'ssl_ca': os.path.join(BASE_DIR, 'certificates', 'DigiCertGlobalRootG2.crt.pem')

            }

            try:
                connection = mysql.connector.connect(**db_config)
                return connection
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
    else:
        @classmethod
        def database_connection(self):
            db_config = {
                'host': '127.0.0.1',
                'user': 'root',
                'password': 'admin',
                'database': 'udyaansaathidata'
            }

            try:
                connection = mysql.connector.connect(**db_config)
                return connection
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
