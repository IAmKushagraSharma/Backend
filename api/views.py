import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import SatelliteInfo, SatNameId, Sensor
from .serializers import SatelliteInfoSerializer, SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import HttpResponse

api_key = 'cE1XhcupGwKMVPa0b7GJ3QbE6aqjkRsfOn8nEB6L'
url = 'https://tle.ivanstanojevic.me/api/tle/?api_key=cE1XhcupGwKMVPa0b7GJ3QbE6aqjkRsfOn8nEB6L&page-size=100'


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'gettle/',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE of satelites'
        },
        {
            'Endpoint': 'tlebyid/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE of satelite by it\'s id'
        },
        {
            'Endpoint': 'tlebyname/name',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE of satelite by it\'s name '
        },
        {
            'Endpoint': 'satellite/',
            'method': 'GET',
            'body': None,
            'description': 'Returns data of All satelite or by it\'s name'
        },
        {
            'Endpoint': 'satellite/<name>',
            'method': 'GET',
            'body': None,
            'description': 'Returns data of All sensor of given satellite'
        },
    ]
    return Response(routes)


def get_Name_id(request):
    response = requests.get('http://127.0.0.1:9000/data')
    data = response.json()['member']
    for satdata in data:
        SatNameId.objects.create(Name=satdata['name'],
                                 SatId=satdata['@id'].strip('https://tle.ivanstanojevic.me/api/tle/'))
    return HttpResponse('<h1>Modles Updated!!</h1>')


@api_view(['GET'])
def get_tle(request):
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_id(request, id):
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/{id}?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_name(request, name):
    Id = SatNameId.objects.filter(Name=name)[0].SatId
    if (Id):
        response = requests.api.get(f'https://tle.ivanstanojevic.me/api/tle/{Id}?&api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def satellite_list(request):
    if request.method == 'GET':
        satellite = SatelliteInfo.objects.all()
        serializer = SatelliteInfoSerializer(satellite, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def satellite_detail(request, name):
    try:
        satellite = SatelliteInfo.objects.get(pk=name)
        print(satellite.Name)
    except satellite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensor = Sensor.objects.filter(SatelliteName=satellite.Name)
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def sensor_detail(request, name, sensor):
    print(pk, sm)

    if request.method == 'GET':
        sensor = Sensor.objects.filter(Q(SatelliteName=name) & Q(SensorName=sensor))
        serializer = SensorallSerializer(sensor, many=True)
        print(serializer.data)
        return Response(serializer.data)
