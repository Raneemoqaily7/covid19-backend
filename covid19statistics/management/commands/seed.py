import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  covid19statistics.models import SumaryStatistics
from django.core.management.base import BaseCommand




def get_query():
    url = 'https://api.covid19api.com/summary'
    r = requests.get(url, headers={'Content-Type':'application/json'})
    data = r.json()

    return data


def seed_total_statistics():
    
    
    total = SumaryStatistics(
        Country = get_query()["Country"],
        TotalConfirmed= get_query()["TotalConfirmed"],
        TotalDeaths= get_query()["TotalDeaths"],
        TotalRecovered =get_query()["TotalRecovered"],


        )
        
    
    total.save()


def clear_data():
      SumaryStatistics.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_total_statistics()
        # clear_data()
        print("completed")













# def get_fishs():
#     url = 'https://api.covid19api.com/world/total'
#     r = requests.get(url, headers={'Content-Type':      
#     'application/json'})
#     fish = r.json()
#     return fish

# def seed_fish():
#     for i in get_fishs():
#         fish = TotalStatistics(
#         TotalConfirmed=i["TotalConfirmed"],
#         TotalDeaths=i["TotalDeaths"],
#         TotalRecovered = i["TotalRecovered"]

#     )
#     fish.save()


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#      seed_fish()
#     # clear_data()
#      print("completed")


# # def totalStatistic ():
 

# #     requests_response = requests.get('https://api.covid19api.com/world/total')

# #     django_response = HttpResponse(
# #     content=requests_response.content,
# #     status=requests_response.status_code,
# #     content_type=requests_response.headers['Content-Type']
# # )

# #     return django_response

