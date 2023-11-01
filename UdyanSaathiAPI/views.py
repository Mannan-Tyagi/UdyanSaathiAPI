
# Create your views here.
# @api_view(['GET'])
# def getRoutes(request):
#     PollutionDAO.get_pollution_by_date_station("2023-07-21","Secretariat, Amaravati - APPCB")
#     return Response('Our Api')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import pollutionModel
from .serializer import PollutionSerializer
from .DBOPS import PollutionDAO

# Your view functions and code go here


@api_view(['GET'])
def getRoutes(request):
    pollutiondata = PollutionDAO.get_pollution_by_date_station("2023-07-21","Secretariat, Amaravati - APPCB")
    serializer = PollutionSerializer(pollutiondata, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)