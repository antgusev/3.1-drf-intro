from django.urls import path


from measurement.views import SensorCreateAPIView, MeasurementsCreateAPIView


urlpatterns = [
     path('sensors/', SensorCreateAPIView.as_view()),
     path('measurments/', MeasurementsCreateAPIView.as_view()), # TODO: зарегистрируйте необходимые маршруты
]
