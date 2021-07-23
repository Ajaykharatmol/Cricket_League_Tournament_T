from django.urls import path
from . import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.countriesList.as_view()),
    path('countries/<int:pk>/', views.countriesDetail.as_view()),
    path('teams/', views.teamsList.as_view()),
    path('teams/<int:pk>/', views.teamsDetail.as_view()),
    path('Players/', views.PlayersList.as_view()),
    path('Players/<int:pk>/', views.PlayersDetail.as_view()),
    path('venue/', views.venueList.as_view()),
    path('venue/<int:pk>/', views.venueDetail.as_view()),
    path('Matches/', views.MatchesList.as_view()),
    path('Matches/<int:pk>/', views.MatchesDetail.as_view()),
    path('Results/', views.ResultsList.as_view()),
    path('Results/<int:pk>/', views.ResultsDetail.as_view()),
    path('Tournament_Score/', views.Tournament_ScoreList.as_view()),
    path('Tournament_Score/<int:pk>/', views.Tournament_ScoreDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)