from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('gettle/', views.get_tle),
    path('tlebyname/<str:name>/', views.tle_by_name),
    path('tlebyid/<str:id>/', views.tle_by_id),
    path('satelliteInfo/', views.SatelliteInfoView.as_view()),
    path('get_Name_id/', views.get_Name_id),
]