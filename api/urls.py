from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('gettle/', views.get_tle),
    path('tlebyname/', views.tle_by_name),
    path('tlebyid/', views.tle_by_id),
    path('satelliteInfo/', views.SatelliteInfoView.as_view())
]