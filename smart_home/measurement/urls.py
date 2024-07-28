from django.urls import path


from measurement.views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementsCreateAPIView


urlpatterns = [
     path('sensors/', SensorListCreateAPIView.as_view()),
     path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
     path('measurments/', MeasurementsCreateAPIView.as_view()), # TODO: зарегистрируйте необходимые маршруты
]
