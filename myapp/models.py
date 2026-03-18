from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    size = models.FloatField(help_text="Area in hectares")


    def __str__(self):
        return self.name


class Location(models.Model):
    farm = models.OneToOneField(Farm, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return f"{self.farm.name} Location"


class EnvironmentalData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    temperature = models.FloatField()
    rainfall = models.FloatField()
    humidity = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Env Data {self.farm.name} ({self.created_at.date()})"


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    soil_type = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Prediction(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.farm.name} → {self.crop.name}"


class Recommendation(models.Model):
    prediction = models.OneToOneField(Prediction, on_delete=models.CASCADE)
    planting_month = models.CharField(max_length=50)
    fertilizer_plan = models.TextField()
    irrigation_plan = models.TextField()
    pest_warning = models.TextField()


    def __str__(self):
        return f"Recommendation for {self.prediction.crop.name}"


