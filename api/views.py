import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

api_key = 'GR71hb8u1YVl15UTOT5ud2fB12PeyPpNUQKd2XMR'


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
            'Endpoint': 'tlebyid/',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE of satelite by it\'s id'
        },
        {
            'Endpoint': 'tlebyname/',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE of satelite by it\'s name   [NOT WORKING CORRECTLY]'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def get_tle(request):
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_id(request):
    satId = 44804
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/{satId}?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_name(request):
    satName = 'CARTOSAT-3'
    response = requests.get(f'https://tle.ivanstanojevic.me/api/tle/?search={satName}&api_key={api_key}')
    return Response(response)