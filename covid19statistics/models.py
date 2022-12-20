from django.db import models

# Create your models here.
class AllRecords (models.Model):
    Country = models.CharField(max_length=30, unique=True)
    TotalConfirmed= models.IntegerField(null=True , blank=True)
    TotalDeaths=models.IntegerField(null=True , blank=True)
    TotalRecovered =models.IntegerField(null=True , blank=True)
    Date=models.DateTimeField()
    def __str__(self):
        return str(self.Country)
    


