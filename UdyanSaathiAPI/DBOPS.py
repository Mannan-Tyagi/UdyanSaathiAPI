from .models import *  # Import the model class
import mysql.connector
from .DBConnection import DBConnection
from datetime import datetime, timedelta

# Get today's date


class PollutionDAO:
    @classmethod    
    def get_pollution_by_date_station(cls, pol_station):
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()

        query = "SELECT distinct State,Station,City,AQI,PM25,PM10,NO2,OZONE,CO,AQI_Quality,Pol_Date FROM\
                 UdyaanSaathiData.hourlydata WHERE Station = %s and Pol_Date in\
                 (SELECT Max(Pol_Date) FROM UdyaanSaathiData.hourlydata WHERE Station = %s)\
        order by AQI desc\
                 limit 1;"
        cursor.execute(query, (pol_station,pol_station,))
        results = cursor.fetchall()

        pollution_list = []

        for row in results:
            pollution_instance = pollutionModel()
            pollution_instance.State = row[0]
            pollution_instance.Station = row[1]
            pollution_instance.City = row[2]
            pollution_instance.AQI = row[3]
            pollution_instance.PM25 = row[4]
            pollution_instance.PM10 = row[5]
            pollution_instance.NO2 = row[6]
            pollution_instance.OZONE = row[7]
            pollution_instance.CO = row[8]
            pollution_instance.AQI_Quality = row[9]

            # Assume that the Pol_Date is in the 10th position of the row
            pollution_instance.Pol_Date = row[10].strftime('%Y-%m-%d %H:%M:%S')
            
            # Call the clean method to format the Date field
            pollution_instance.clean()

            pollution_list.append(pollution_instance)

        cursor.close()
        connection.close()

        return pollution_list

    @classmethod    
    def get_stations(cls, stationName,pol_Date):
       
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()
        stationName = '%' + stationName + '%'
        
        query = "SELECT DISTINCT Station FROM UdyaanSaathiData.hourlydata WHERE City LIKE %s and Pol_Date in\
                 (SELECT Max(Pol_Date) FROM UdyaanSaathiData.hourlydata WHERE City LIKE %s);"
        
       
        cursor.execute(query, (stationName,stationName,))
        results = cursor.fetchall()

        station_list = []

        for row in results:
            pollution_instance = stationModel()
            pollution_instance.Station = row[0]

            station_list.append(pollution_instance)

        cursor.close()
        connection.close()

        return station_list
    @classmethod
    def get_Top10Cities(cls,fromdate,todate):
       
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()   

        # stationName = '%' + stationName + '%'
        
        query = "SELECT City, MAX(AQI) AS AQI, MAX(PM25) AS PM25, MAX(PM10) AS PM10, MAX(CO) AS CO, MAX(OZONE) AS OZONE, MAX(SO2) AS SO2, MAX(NO2) AS NO2, MAX(NH3) AS NH3\
                FROM UdyaanSaathiData.pollutiondata\
                WHERE pol_Date BETWEEN %s AND %s \
                GROUP BY City\
                ORDER BY AQI DESC\
                LIMIT 6;"
        
       
        cursor.execute(query,(fromdate,todate,))
        results = cursor.fetchall()

        Top10Cities_List = []

        for row in results:
            pollution_instance = Top10CitiesModel()
            pollution_instance.City = row[0]
            pollution_instance.AQI = row[1]
            pollution_instance.PM25 = row[2]
            pollution_instance.PM10 = row[3]
            pollution_instance.CO = row[4]
            pollution_instance.OZONE = row[5]
            pollution_instance.SO2 = row[6]
            pollution_instance.NO2 = row[7]
            pollution_instance.NH3 = row[8]

            Top10Cities_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return Top10Cities_List
    
    @classmethod
    def get_Top10LeastPollutedCities(cls,fromdate,todate):
       
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()   

        # stationName = '%' + stationName + '%'
        
        query = "SELECT City, Min(AQI) AS AQI, Min(PM25) AS PM25, Min(PM10) AS PM10, Min(CO) AS CO, Min(OZONE) AS OZONE, Min(SO2) AS SO2, Min(NO2) AS NO2, Min(NH3) AS NH3\
                FROM UdyaanSaathiData.pollutiondata\
                WHERE pol_Date BETWEEN %s AND %s\
                GROUP BY City\
                ORDER BY AQI asc\
                LIMIT 6;"
        
       
        cursor.execute(query,(fromdate,todate,))
        results = cursor.fetchall()

        Top10LeastCities_List = []

        for row in results:
            pollution_instance = Top10LeastCitiesModel()
            pollution_instance.City = row[0]
            pollution_instance.AQI = row[1]
            pollution_instance.PM25 = row[2]
            pollution_instance.PM10 = row[3]
            pollution_instance.CO = row[4]
            pollution_instance.OZONE = row[5]
            pollution_instance.SO2 = row[6]
            pollution_instance.NO2 = row[7]
            pollution_instance.NH3 = row[8]

            Top10LeastCities_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return Top10LeastCities_List
    
    @classmethod
    def get_graphData(cls,pol_Station,fromdate,todate):
       
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
            pollution_instance.Pol_Date = row[9].strftime('%Y-%m-%d')
            GraphData_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return GraphData_List
    
    def get_metrocitiesdata(pol_Station):
        today = datetime.now()

        yesterday = today - timedelta(days=1)

        formatted_date = yesterday.strftime('%Y-%m-%d')

        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()   

        # stationName = '%' + stationName + '%'
        
        query = "SELECT\
                City,\
                ROUND(AVG(AQI), 2) AS AQI,\
                ROUND(AVG(NH3), 2) AS NH3,\
                ROUND(AVG(PM10), 2) AS PM10,\
                ROUND(AVG(PM25), 2) AS PM25,\
                ROUND(AVG(NO2), 2) AS NO2,\
                ROUND(AVG(SO2), 2) AS SO2,\
                ROUND(AVG(CO), 2) AS CO,\
                ROUND(AVG(OZONE), 2) AS OZONE\
                FROM\
                UdyaanSaathiData.pollutiondata\
                WHERE\
                Pol_Date = %s\
                AND City IN ('Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata', 'Mumbai', 'Delhi')\
                GROUP BY\
                City\
                ORDER BY\
                AQI DESC;"
        
       
        cursor.execute(query,(formatted_date,))
        results = cursor.fetchall()

        TopMetroCitiesModel_List = []

        for row in results:
            pollution_instance = TopMetroCitiesModel()
            pollution_instance.City = row[0]
            pollution_instance.AQI = row[1]
            pollution_instance.PM25 = row[2]
            pollution_instance.PM10 = row[3]
            pollution_instance.CO = row[4]
            pollution_instance.OZONE = row[5]
            pollution_instance.SO2 = row[6]
            pollution_instance.NO2 = row[7]
            pollution_instance.NH3 = row[8]

            TopMetroCitiesModel_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return TopMetroCitiesModel_List
    @classmethod
    def get_aqicaldata(cls,pol_Station):
       
        dbconnection = DBConnection()
        connection = dbconnection.database_connection()
        cursor = connection.cursor()   

        # stationName = '%' + stationName + '%'
        
        query = "SELECT City,AQI,Pol_Date\
                FROM UdyaanSaathiData.pollutiondata\
                WHERE Station = 'Secretariat, Amaravati - APPCB' AND Pol_Date LIKE '%2023%'"
        
        cursor.execute(query,())
        results = cursor.fetchall()

        AqiCalendarModel_List = []

        for row in results:
            pollution_instance = AqiCalendarModel()
            pollution_instance.City = row[0]
            pollution_instance.AQI = row[1]
            pollution_instance.Pol_Date = row[2].strftime('%Y-%m-%d')
            AqiCalendarModel_List.append(pollution_instance)

        cursor.close()
        connection.close()

        return AqiCalendarModel_List