from django.urls import path
from . import views

# ONLY FOR DEBUG 
#**************START*********************
from .DBOPS import PollutionDAO
from .serializer import PollutionSerializer
pollutiondata = PollutionDAO.get_pollution_by_date_station("Knowledge Park - III, Greater Noida - UPPCB")
# GraphData = PollutionDAO.get_graphData("Knowledge Park - III, Greater Noida - UPPCB","2023-12-01","2023-12-07")
#GraphData = PollutionDAO.get_graphData(pol_Station,fromdate,todate)
serializer = PollutionSerializer(pollutiondata, many=True)


#*************END**********************




urlpatterns = [
    path('get-pollution-by-date-station/', views.getRoutes, name="routes"),
    path('get-stations/', views.getStations, name="routes"),
    path('get-Top10Cities/', views.get_Top10Cities, name="routes"),
    path('get-Top10LeastPollutedCities/', views.get_Top10LeastPollutedCities, name="routes"),
    path('get-GraphData/', views.get_GraphData, name="routes"),
    path('get-MetroCityData/', views.get_metrocitiesdata, name="routes"),
    path('get-AqiCalData/', views.get_AqiCalendarData, name="routes"),


]
