from django.urls import path
from . import views

urlpatterns = [
    path('get-pollution-by-date-station/', views.getRoutes, name="routes"),
    path('get-stations/', views.getStations, name="routes"),
    path('get-Top10Cities/', views.get_Top10Cities, name="routes"),
    path('get-Top10LeastPollutedCities/', views.get_Top10LeastPollutedCities, name="routes"),
    path('get-GraphData/', views.get_GraphData, name="routes"),
    path('get-MetroCityData/', views.get_metrocitiesdata, name="routes"),
    path('get-AqiCalData/', views.get_AqiCalendarData, name="routes"),


]
