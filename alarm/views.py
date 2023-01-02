from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from alarm.models import UserAlarm, User, OnOffRecord
from alarm.serializers import AlarmSerializer, OnOffRecordSerializer


class AlarmAPIView(APIView):

    def get(self, request):  # 알람 조회

        user_id = request.query_params['user_id']

        user = User.objects.get(id=user_id)

        alarms = UserAlarm.objects.filter(user=user)


        print(alarms.query)

        response = []
        for alarm in alarms:
            response.append({
                'alarm_id': alarm.id,
                'yen_price': alarm.yen_price,
                'is_active': OnOffRecord.objects.filter(user_alarm_id=alarm.id).last().is_active
            })

        return Response({'alarms': response}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # 알람 등록
        data = {
            'currency_price': request.data.get('currency_price'),
            'which_currency': request.data.get('which_currency'),
            'user': request.data.get('user_id')
        }
        serializer = AlarmSerializer(data=data)
        if serializer.is_valid():
            serializer.save() #save()를 통해 serializer의 create() 실행, 새로운 db 인스턴스 생성
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlarmUpdateAPIView(APIView):

    def post(self, request, *args, **kwargs):   # 온오프레코드 추가
        print(request.data.get('is_active'), kwargs['pk'])
        data = {
            'is_active': request.data.get('is_active'),
            'user_alarm': kwargs['pk']
        }
        serializer = OnOffRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



