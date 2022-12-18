from django.db import models

# Create your models here.
class TotalStatistics (models.Model):
    TotalConfirmed= models.IntegerField()
    TotalDeaths=models.IntegerField()
    TotalRecovered =models.IntegerField()

    def __str__(self):
        return str(self.TotalConfirmed)