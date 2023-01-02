from django.urls import path
from . import views

urlpatterns = [
   path('', views.AlarmAPIView.as_view()),
   path('<int:pk>/', views.AlarmUpdateAPIView.as_view()),
]
