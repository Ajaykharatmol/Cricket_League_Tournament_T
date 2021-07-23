from django.db import models


class countries_table(models.Model):
    Nations = models.CharField(max_length=120, unique=True)
    Tournament = models.CharField(max_length=220)
    Period = models.IntegerField()
    

    def __str__(self):
        return self.Nations

class teams_table(models.Model):
    Profile = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.Profile
        
class Players_Table(models.Model):
    Profile = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.Profile


class venue_table(models.Model):
    Date = models.DateField(max_length=120, unique=True)
    Match = models.CharField(max_length=220)
    Time = models.TimeField(max_length=220)
    venue = models.CharField(max_length=220)

    def __str__(self):
        return self.Date

class Matches_table(models.Model):
    List_of_Matches = models.CharField(max_length=120, unique=True)
    Team_Details = models.DateField(max_length=120, unique=True)
    Looser = models.CharField(max_length=220)
    Man_of_the_Match = models.TimeField(max_length=220)
    Bowler_of_the_Match = models.CharField(max_length=220)
    Best_Fielder = models.CharField(max_length=220)
    def __str__(self):
        return self.List_of_Matches
        
class Results_Table(models.Model):
    winning_team = models.CharField(max_length=120, unique=True)
    loosing_team = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.winning_team

class Tournament_Score_Table(models.Model):
    Position = models.IntegerField()
    Team = models.CharField(max_length=120, unique=True)
    Series_played = models.IntegerField()
    Won = models.IntegerField()
    Lost = models.IntegerField()
    Total_points = models.IntegerField()
    def __str__(self):
        return self.Position



