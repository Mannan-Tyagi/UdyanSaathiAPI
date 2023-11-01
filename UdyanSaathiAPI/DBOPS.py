from .models import pollutionModel  # Import the model class
import mysql.connector

class PollutionDAO:
    @classmethod
    def get_pollution_by_date_station(cls, pol_date, pol_station):
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Impetus@123',
            'database': 'PollutionData'
        }

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT State, City,AQI,PM25,PM10,AQI_Quality FROM pollutiondata.udyansaathiapi_pollutoin WHERE Pol_Date = %s AND Station = %s"
        cursor.execute(query, (pol_date, pol_station))
        results = cursor.fetchall()

        pollution_list = []

        for row in results:
            pollution_instance = pollutionModel()
            pollution_instance.State = row[0]
            pollution_instance.City = row[1]
            pollution_instance.AQI = row[2]
            pollution_instance.PM25 = row[3]
            pollution_instance.PM10 = row[4]
            pollution_instance.AQI_Quality = row[5]

            pollution_list.append(pollution_instance)

        cursor.close()
        connection.close()

        return pollution_list
