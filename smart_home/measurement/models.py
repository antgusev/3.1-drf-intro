from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    description = models.CharField(max_length=50, verbose_name='description')
    # measurments = models.ForeignKey(Measurement, on_delete=models.CASCADE)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')


