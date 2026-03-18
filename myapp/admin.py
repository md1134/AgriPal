from django.contrib import admin

# Register your models here.
from.models import Farm, EnvironmentalData, Crop, Prediction, Recommendation

admin.site.register(Farm)
admin.site.register(EnvironmentalData)
admin.site.register(Crop)
admin.site.register(Prediction)
admin.site.register(Recommendation)