from django.urls import path
from . import views
from .views import RegisterUserAPIView


urlpatterns = [
    path('', views.getRoutes),
	path('register/',RegisterUserAPIView.as_view()),
    path('gettle/', views.get_tle),
    path('tlebyname/<str:name>/', views.tle_by_name),
    path('tlebyid/<str:id>/', views.tle_by_id),
    path('orbital_elements/<str:satName>/', views.orbital_elements),
    path('satellite/', views.satellite_list),
    path('satellite/<name>', views.satellite_detail),
    path('satellite/<name>/<sensor>', views.sensor_detail),
    path('sensor/', views.sensor_list),
    path('sensor/<name>', views.satellite_name),
    path('sensor/<name>/<sensor>', views.sensor_detail),
    path('application/', views.application_list),
    path('application/<applicationname>', views.application_to_sensor_details),
    path('orbital_elements_by_id', views.orbital_elements_by_id),
    path('orbital_elements_by_name', views.orbital_elements_by_name),



]


