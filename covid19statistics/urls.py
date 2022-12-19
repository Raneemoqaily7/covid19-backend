from django.urls import path 
from . import views

urlpatterns = [
    path ( 'world/total',views.get_total , name='totalStatistic'),
    path ( 'world/summary',views.get_summary , name='summary'),
    path ( 'country/<country>/status/confirmed/from=<startdate>/to=<enddate>',views.get_query ),
    

]
