from http.client import HTTPResponse
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from covid19statistics.api.serializers import AllRecordsSerializer
from .models import AllRecords



@api_view(['GET'])

def get_total(req):

    if req.method == 'GET':
       
        url = "https://api.covid19api.com/world/total"

        response = requests.request("GET", url)
        data = response.json()
    return Response(data)





@api_view(['GET'])

def get_allrecords(req):

    if req.method == 'GET':
       
        records  = AllRecords.objects.all()
        print(records ,"recordsss ")
        serializer = AllRecordsSerializer (records , many =True )
        return Response (serializer.data ,status = status.HTTP_200_OK)
    return Response (serializer.data  ,status= status.HTTP_404_NOT_FOUND)



 
@api_view(['POST'])

def post_addtomyrecords(req,data):

    if req.method == 'POST':
          data =json.loads(data)
          y = {"Country":data["Country"],"TotalConfirmed":data["TotalConfirmed"],"TotalDeaths":data["TotalDeaths"],"TotalRecovered":data["TotalRecovered"],"Date":data["Date"]}
          serializer = AllRecordsSerializer(data =y)
 
          if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED )
        
    return Response (serializer.data  ,status= status.HTTP_404_NOT_FOUND)

    
 




 


@api_view(['GET' ,"POST"])

def get_country_statistic(req,country,startdate,enddate):
    if req.method =="GET":
        text = {"sura" : "ranee"}
        headers ={"name" : "raneem"}
        payload={"name" : "rrrr"}
        url =f"https://api.covid19api.com/country/{country}/status/confirmed?from={startdate}T00:00:00Z&to={enddate}T00:00:00Z"
        
     
        response = requests.request("GET" ,url ,headers=headers , data=payload  )
        return Response (response.json())
    


@api_view(['GET'])

def get_summary(req):

    if req.method == 'GET':
       
        url = "https://api.covid19api.com/summary"

        response = requests.request("GET", url)
        data = response.json()
    return Response(data)





@api_view (['DELETE'])

def delete_id (request , id): 
    

    record = AllRecords.objects.get (id = id)
    if request.method == "DELETE":
        record.delete()
        return Response (status.HTTP_204_NO_CONTENT)










