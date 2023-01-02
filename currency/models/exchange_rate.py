from django.db import models
from JPYAlarm.common_models import BaseModel


class ExchangeRate(BaseModel):
    """
    크롤링 데이터 테이블
    """
    code = models.CharField(max_length=20)
    exchangerate = models.FloatField()
