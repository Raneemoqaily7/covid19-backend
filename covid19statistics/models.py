from django.db import models

# Create your models here.
class SumaryStatistics (models.Model):
    Country = models.CharField(max_length=30)
    TotalConfirmed= models.IntegerField()
    TotalDeaths=models.IntegerField()
    TotalRecovered =models.IntegerField()

    def __str__(self):
        return str(self.Country)
    


