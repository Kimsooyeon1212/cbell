from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'created_datetime', 'device_type', 'device_token')


class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlarm
        fields = ('id', 'currency_price', 'which_currency', 'user')

    def create(self, validated_data):
        # user_alarm 생성
        user_alarm = UserAlarm.objects.create(**validated_data)

        # onoffrecord 생성(초기값 1로 세팅)
        on_off_record = OnOffRecord.objects.create(is_active=1, user_alarm=user_alarm)

        return user_alarm


class OnOffRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnOffRecord
        fields = ('id', 'is_active', 'user_alarm')