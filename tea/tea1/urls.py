from django.urls import path
from .views import (
    HomeView,
    PredictionView
)

app_name = 'tea1'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('pred/',PredictionView.as_view(),name='pred')
]