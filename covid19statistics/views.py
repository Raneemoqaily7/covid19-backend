from http.client import HTTPResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import TotalStatistics
from django.core.management.base import BaseCommand


@api_view(['GET'])

def get_total(req):

    if req.method == 'GET':
       
        url = "https://api.covid19api.com/world/total"

        response = requests.request("GET", url)
        data = response.json()
    return Response(data)




#In the index view of user.views: 
@api_view(['GET' ,"POST"])

def get_query(req,country,startdate,enddate):
    print (country , "coooontryyyy")
    if req.method =="GET":
        text = {"sura" : "raneem"}
        headers ={"name" : "sura"}
        payload={"name" : "sura"}
        print (country , "llllllllllllllllll")
        url =f"https://api.covid19api.com/country/{country}/status/confirmed?from={startdate}T00:00:00Z&to={enddate}T00:00:00Z"
        
     
        response = requests.request("GET" ,url ,headers=headers , data=payload , text = text )
        return Response (response.json())
    


@api_view(['GET'])

def get_summary(req):

    if req.method == 'GET':
       
        url = "https://api.covid19api.com/summary"

        response = requests.request("GET", url)
        data = response.json()
    return Response(data)







# def seed_total_statistics():
#     for i in get_query():
#         total = TotalStatistics(
#         TotalConfirmed=i["TotalConfirmed"],
#         TotalDeaths=i["TotalDeaths"],
#         TotalRecovered =i["TotalRecovered"],
#   )
#     total.save()


# def clear_data():
#       TotalStatistics.objects.all().delete()


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         seed_total_statistics()
#     # clear_data()
#         print("completed")













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

