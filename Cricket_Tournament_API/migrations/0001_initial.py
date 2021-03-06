# Generated by Django 3.2.5 on 2021-07-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countries_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nations', models.CharField(max_length=120, unique=True)),
                ('Tournament', models.CharField(max_length=220)),
                ('Period', models.IntegerField(max_length=220)),
                ('Current_Tropy_Holder', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Matches_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('List_of_Matches', models.CharField(max_length=120, unique=True)),
                ('Team_Details', models.DateField(max_length=120, unique=True)),
                ('Looser', models.CharField(max_length=220)),
                ('Man_of_the_Match', models.TimeField(max_length=220)),
                ('Bowler_of_the_Match', models.CharField(max_length=220)),
                ('Best_Fielder', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Players_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Results_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_team', models.CharField(max_length=120, unique=True)),
                ('loosing_team', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teams_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament_Score_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.IntegerField(max_length=120, unique=True)),
                ('Team', models.CharField(max_length=120, unique=True)),
                ('Series_played', models.IntegerField(max_length=220)),
                ('Won', models.IntegerField(max_length=220)),
                ('Lost', models.IntegerField(max_length=220)),
                ('Total_points', models.IntegerField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='venue_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(max_length=120, unique=True)),
                ('Match', models.CharField(max_length=220)),
                ('Time', models.TimeField(max_length=220)),
                ('venue', models.CharField(max_length=220)),
            ],
        ),
    ]
