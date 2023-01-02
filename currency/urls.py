from django.urls import path
from . import views

urlpatterns = [
   path('', views.ExchangeRateAPIView.as_view()),
]
