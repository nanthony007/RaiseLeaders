# Generated by Django 3.0.3 on 2020-07-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_auto_20200613_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='belt_level',
            field=models.CharField(choices=[('White', 'White'), ('White/Yellow', 'White/Yellow'), ('White/Black', 'White/Black'), ('Yellow', 'Yellow'), ('Yellow/Black', 'Yellow/Black'), ('Orange', 'Orange'), ('Orange/Black', 'Orange/Black'), ('Green', 'Green'), ('Green/Black', 'Green/Black'), ('Purple', 'Purple'), ('Purple/Black', 'Purple/Black'), ('Blue', 'Blue'), ('Blue/Black', 'Blue/Black'), ('Brown', 'Brown'), ('Brown/Black', 'Brown/Black'), ('Red', 'Red'), ('Red/Black', 'Red/Black'), ('Candidate', 'Candidate'), ('Black', 'Black')], default='White', max_length=25),
        ),
    ]
