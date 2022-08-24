from django.urls import path
from . import views
from .views import RegisterUserAPIView


urlpatterns = [
    path('', views.getRoutes),
    path('index/',views.index),
    path('register/',RegisterUserAPIView.as_view()),
    path('gettle/', views.get_tle),
    path('tlebyname/<str:name>/', views.tle_by_name),
    path('tlebyid/<str:id>/', views.tle_by_id),
    path('satellite/', views.satellite_list),
    path('satellite/<name>', views.satellite_detail),

    path('satellite/<name>/<sensor>', views.sensor_detail),
    #path('application/',views.satellite_application)

    path('satellite/<name>/<sensor>', views.satellite_detail),
]


