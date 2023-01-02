
from django.db import models
from JPYAlarm.common_models import BaseModel


class User(BaseModel):
    """
    user 이자 device
    """

    class DeviceTypes(models.TextChoices):
        IOS = 'ios', 'ios'
        ANDROID = 'aos', 'android'

    device_type = models.CharField(max_length=4, choices=DeviceTypes.choices)
    device_token = models.CharField(max_length=100)
