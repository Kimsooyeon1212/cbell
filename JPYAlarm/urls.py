
from django.contrib import admin
from django.urls import path, include
from alarm.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alarms/', include('alarm.urls')),
    path('currency/', include('currency.urls')),
]
