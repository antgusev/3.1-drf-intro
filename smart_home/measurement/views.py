# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import generics


from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer

# class SensorView(generics.ListCreateAPIView):
#     def get(self, request, pk):
#         sensor = Sensor.objects.get(pk=pk)
#         ser = SensorDetailSerializer(sensor)
#         return Response(ser.data)

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def post(self, request, *args, **kwargs):
    #     new_sensor = Sensor.objects.create(
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #     return self.create(request, new_sensor)


class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer