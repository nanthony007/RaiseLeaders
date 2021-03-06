# Generated by Django 3.0.3 on 2020-05-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_code', models.CharField(max_length=5)),
                ('class_datetime', models.DateTimeField()),
                ('class_label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Terminology', 'Terminology'), ('Techniques', 'Techniques'), ('Poomsae', 'Poomsae'), ('Workouts', 'Workouts'), ('Acrobatics', 'Acrobatics'), ('Extras', 'Extras')], max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
                ('difficulty', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=25)),
                ('belt_level', models.CharField(choices=[('White', 'White'), ('White/Yellow', 'White/Yellow'), ('White/Black', 'White/Black'), ('Yellow', 'Yellow'), ('Yellow/Black', 'Yellow/Black'), ('Orange', 'Orange'), ('Orange/Black', 'Orange/Black'), ('Green', 'Green'), ('Green/Black', 'Green/Black'), ('Purple', 'Purple'), ('Purple/Black', 'Purple/Black'), ('Blue', 'Blue'), ('Blue/Black', 'Blue/Black'), ('Brown', 'Brown'), ('Brown/Black', 'Brown/Black'), ('Red', 'Red'), ('Red/Black', 'Red/Black')], max_length=25)),
                ('curriculum', models.BooleanField()),
                ('video_link', models.CharField(max_length=250)),
            ],
        ),
    ]
