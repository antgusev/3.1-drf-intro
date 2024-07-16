from django.contrib import admin
# from django.forms import BaseInlineFormSet

# Register your models here.
from measurement.models import Measurement, Sensor


class MeasurementInline(admin.TabularInline):
    model = Measurement
    

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]
