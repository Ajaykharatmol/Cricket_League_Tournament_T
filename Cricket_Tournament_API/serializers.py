from .models import  countries_table,teams_table,Players_Table,venue_table,Matches_table,Results_Table,Tournament_Score_Table
from rest_framework import serializers


class  countries_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model =  countries_table
        fields = '__all__'

class teams_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = teams_table
        fields = '__all__'

class Players_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players_Table
        fields = '__all__'

class venue_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = venue_table
        fields = '__all__'

class Matches_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches_table
        fields = '__all__'

class Results_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results_Table
        fields = '__all__'

class Tournament_Score_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament_Score_Table
        fields = '__all__'