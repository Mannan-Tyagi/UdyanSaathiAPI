
# Create your views here.
# @api_view(['GET'])
# def getRoutes(request):
#     PollutionDAO.get_pollution_by_date_station("2023-07-21","Secretariat, Amaravati - APPCB")
#     return Response('Our Api')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import pollutionModel
from .serializer import *
from .DBOPS import PollutionDAO

# Your view functions and code go here


@api_view(['GET'])
def getRoutes(request):
    
    # pol_Date = request.GET.get('pol_Date')
    pol_Station = request.GET.get('pol_Station')
    pollutiondata = PollutionDAO.get_pollution_by_date_station(pol_Station)
    serializer = PollutionSerializer(pollutiondata, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getStations(request):
    
    pol_Station = request.GET.get('pol_Station')
    pol_Date = request.GET.get('pol_Date')
    # pol_Date = '2023-11-18 23:00:00'
    stationdata = PollutionDAO.get_stations(pol_Station,pol_Date)
    serializer = StationSerializer(stationdata, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_Top10Cities(request):
    fromdate = request.GET.get('from_date')
    todate = request.GET.get('to_date')
    Top10CityData = PollutionDAO.get_Top10Cities(fromdate,todate)
    serializer = Top10CitiesSerializer(Top10CityData, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_Top10LeastPollutedCities(request):
    fromdate = request.GET.get('from_date')
    todate = request.GET.get('to_date')
    Least10CityData = PollutionDAO.get_Top10LeastPollutedCities(fromdate,todate)
    serializer = Top10LeastCitiesSerializer(Least10CityData, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_GraphData(request):
    fromdate = request.GET.get('from_date')
    todate = request.GET.get('to_date')
    pol_Station = request.GET.get('pol_Station')
    GraphData = PollutionDAO.get_graphData(pol_Station,fromdate,todate)
    serializer = GraphSerializer(GraphData, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def get_metrocitiesdata(request):
    # fromdate = request.GET.get('from_date')
    # todate = request.GET.get('to_date')
    pol_Station = request.GET.get('pol_Station')
    metroData = PollutionDAO.get_metrocitiesdata(pol_Station)
    serializer = TopMetroCitiesSerializer(metroData, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def get_AqiCalendarData(request):
    # fromdate = request.GET.get('from_date')
    # todate = request.GET.get('to_date')
    pol_Station = request.GET.get('pol_Station')
    aqicalData = PollutionDAO.get_aqicaldata(pol_Station)
    serializer = AqiCalendarSerializer(aqicalData, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)