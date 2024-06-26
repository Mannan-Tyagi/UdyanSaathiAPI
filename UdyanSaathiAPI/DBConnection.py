import mysql.connector


# class DBConnection:
#     
class DBConnection:
    # keyword = "Azure"
    keyword = "Local"
    if(keyword == "Azure"):
        @classmethod
        def database_connection(self):
            db_config = {
                'host': 'mysqlmannan01.mysql.database.azure.com',
                'user': 'mannan',
                'password': 'Khetan@123',
                'database': 'udyaansaathidata',
                'client_flags': [mysql.connector.ClientFlag.SSL],
                'ssl_ca': '/var/www/html/DigiCertGlobalRootG2.crt.pem'

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
