from rest_framework import serializers
from covid19statistics.models import AllRecords


class AllRecordsSerializer (serializers.ModelSerializer):

    class Meta :
        model =  AllRecords
        fields = ["id" , "Country", "Date"]

