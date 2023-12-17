from models import *  # Import the model class
import mysql.connector
from .DBConnection import DBConnection
from datetime import datetime, timedelta

def get_testData(pol_Station,fromdate,todate):
       
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()   

        # stationName = '%' + stationName + '%'
        
        query = "SELECT DISTINCT City, AQI,PM25,PM10,CO,OZONE,SO2,NO2,NH3,Pol_Date FROM UdyaanSaathiData.pollutiondata\
                 WHERE Station = %s\
                 AND pol_Date BETWEEN %s AND %s;"
        
        cursor.execute(query,(pol_Station,fromdate,todate,))
        results = cursor.fetchall()

        GraphData_List = []

        for row in results:
            pollution_instance = graphDataModel()
            pollution_instance.City = row[0]
            pollution_instance.AQI = row[1]
            pollution_instance.PM25 = row[2]
            pollution_instance.PM10 = row[3]
            pollution_instance.CO = row[4]
            pollution_instance.OZONE = row[5]
            pollution_instance.SO2 = row[6]
            pollution_instance.NO2 = row[7]
            pollution_instance.NH3 = row[8]
            pollution_instance.Pol_Date = row[9]
            GraphData_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return GraphData_List

get_testData("Knowledge%20Park - III, Greater Noida - UPPCB","2023-12-01","2023-12-07")