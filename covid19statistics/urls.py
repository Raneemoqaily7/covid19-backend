from django.urls import path 
from . import views

urlpatterns = [
    path ( 'world/total',views.get_total , name='totalStatistic'),
    path ( 'world/summary',views.get_summary , name='summary'),
    path ( 'getAllRecords',views.get_allrecords , name='allrecords'),
    path ( 'addtomyrecords/<data>',views.post_addtomyrecords , name='addtomyrecords'),
    path ( 'country/<country>/status/confirmed/from=<startdate>/to=<enddate>',views.get_country_statistic ),
    path('delete/<id>/', views.delete_id),
    

]
