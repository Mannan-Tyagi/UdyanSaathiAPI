from django.urls import path
from . import views

# # ONLY FOR DEBUG 
# #**************START*********************
# from .DBOPS import PollutionDAO
# from .serializer import *
# # pollutiondata = PollutionDAO.get_pollution_by_date_station("Knowledge Park - III, Greater Noida - UPPCB")
# Mldata =  PollutionDAO.get_mldata("Knowledge Park - III, Greater Noida - UPPCB")
# serializer = MlSerializer(Mldata, many=True)
# # serializer = MlSerializer(pollutiondata, many=True)


# #*************END**********************




urlpatterns = [
    path('get-pollution-by-date-station/', views.getRoutes, name="routes"),
    path('get-stations/', views.getStations, name="routes"),
    path('get-Top10Cities/', views.get_Top10Cities, name="routes"),
    path('get-Top10LeastPollutedCities/', views.get_Top10LeastPollutedCities, name="routes"),
    path('get-GraphData/', views.get_GraphData, name="routes"),
    path('get-MetroCityData/', views.get_metrocitiesdata, name="routes"),
    path('get-AqiCalData/', views.get_AqiCalendarData, name="routes"),
    path('get-MLData/', views.get_mldata, name="routes"),
    path('get-MapData/', views.get_mapdata, name="routes"),
    path('get-allStations/', views.getAllStations, name="routes"),
]
