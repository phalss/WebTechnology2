from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name="prices"),
    path('chart/',views.simple_chart,name="chart"),
    path('api/', views.api_periodic_refresh, name="api_periodic_refresh"),
]