# Generated by Django 3.0.3 on 2020-06-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_auto_20200531_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.CharField(default='Description not available.', max_length=250, null=True),
        ),
    ]
