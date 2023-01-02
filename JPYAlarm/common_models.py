
from django.db import models


class BaseModel(models.Model):

    id = models.BigAutoField(primary_key=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
