
from django.db import models
from JPYAlarm.common_models import BaseModel


class UserAlarm(BaseModel):
    """
    유저가 등록한 알람
    """
    which_currency = models.CharField(max_length=10, blank=True) #어떤 통화 알림받을래
    currency_price = models.FloatField() #얼마일때 알림받을래
    user = models.ForeignKey('alarm.User', related_name='alarms', on_delete=models.PROTECT)


class OnOffRecord(BaseModel):
    user_alarm = models.ForeignKey('alarm.UserAlarm', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

