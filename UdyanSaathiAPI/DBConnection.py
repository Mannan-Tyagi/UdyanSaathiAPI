import mysql.connector
import os
import environ

class DBConnection:
    # USING KEYWORDS TO INSTANTLY SWITCH BETWEEN AZURE AND LOCAL DATABASE
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = environ.Env()
    
    # Read environment variables from .env file if present
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    # Get the database keyword from environment variable
    keyword = env('DATABASE_KEYWORD', default='Local')
    # keyword = "Azure"
    # keyword = "Azure"
    # CONDITION TO CHECK THE DATABASE KEYWORD TO USE
    if(keyword == "Azure"):
        #CONFIGURATION FOR DATABASE CONNECTION 
        @classmethod
        def database_connection(self):
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_config = {
                'host': environ.env('AZURE_DATABASE_HOST'),
                'user': 'mannan',
                'password': 'Khetan@123',
                'database': 'udyaansaathidata',
                'client_flags': [mysql.connector.ClientFlag.SSL],
                'ssl_ca': os.path.join(BASE_DIR, 'certificates', 'DigiCertGlobalRootG2.crt.pem')

            }
            # CONNECTING TO DATABASE
            try:
                connection = mysql.connector.connect(**db_config)
                return connection
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
    else:
        #CONFIGURATION FOR DATABASE CONNECTION 
        @classmethod
        def database_connection(self):
            db_config = {
                'host': '127.0.0.1',
                'user': 'root',
                'password': 'admin',
                'database': 'udyaansaathidata'
            }
            # CONNECTING TO DATABASE
            try:
                connection = mysql.connector.connect(**db_config)
                return connection
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
