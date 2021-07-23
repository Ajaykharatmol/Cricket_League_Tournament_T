from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import countries_table,teams_table,Players_Table,venue_table,Matches_table,Results_Table,Tournament_Score_Table
from rest_framework import generics, status
from .serializers import countries_tableSerializer,teams_tableSerializer,Players_TableSerializer,venue_tableSerializer,Matches_tableSerializer,Results_TableSerializer,Tournament_Score_TableSerializer
from django.utils import timezone  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view



class countriesList(APIView):
    def get(self, request, format=None):

        snippets = countries_table.objects.all()
        serializer = countries_tableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = countries_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class countriesDetail(APIView):
    def get_object(self, pk):
        try:
            return countries_table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = countries_tableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = countries_tableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class teamsList(APIView):
    def get(self, request, format=None):

        snippets = teams_table.objects.all()
        serializer = teams_tableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = teams_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class teamsDetail(APIView):
    def get_object(self, pk):
        try:
            return teams_table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = teams_tableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = teams_tableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayersList(APIView):
    def get(self, request, format=None):

        snippets = Players_Table.objects.all()
        serializer = Players_TableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Players_TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlayersDetail(APIView):
    def get_object(self, pk):
        try:
            return Players_Table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Players_TableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Players_TableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class venueList(APIView):
    def get(self, request, format=None):

        snippets = venue_table.objects.all()
        serializer = venue_tableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = venue_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class venueDetail(APIView):
    def get_object(self, pk):
        try:
            return venue_table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = venue_tableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = venue_tableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MatchesList(APIView):
    def get(self, request, format=None):

        snippets = Matches_table.objects.all()
        serializer = Matches_tableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Matches_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MatchesDetail(APIView):
    def get_object(self, pk):
        try:
            return Matches_table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Matches_tableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Matches_tableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResultsList(APIView):
    def get(self, request, format=None):

        snippets = Results_Table.objects.all()
        serializer = Results_TableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Results_TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResultsDetail(APIView):
    def get_object(self, pk):
        try:
            return Results_Table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Results_TableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Results_TableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Tournament_ScoreList(APIView):
    def get(self, request, format=None):

        snippets = Tournament_Score_Table.objects.all()
        serializer = Tournament_Score_TableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Tournament_Score_TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Tournament_ScoreDetail(APIView):
    def get_object(self, pk):
        try:
            return Tournament_Score_Table.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Tournament_Score_TableSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Tournament_Score_TableSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
#from .models import Books
#from .forms import BooksForm
from django.template import Context
from django.shortcuts import render
import requests

#def index(request):
    #emp = Books.objects.all()
    #return render(request,'dashboard.html')

def index(request):
    res = requests.get('https://crickettournamentapp.herokuapp.com/countries/')

    response_data = res.json()
    
    #print(response_data)
    products = response_data[0]
    print(products)
   
    if res.status_code == 200:
        return render(request, 'dashboard.html',
                      {"products": products})
    else:
        print("error")



