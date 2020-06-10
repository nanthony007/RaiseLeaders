# Generated by Django 3.0.3 on 2020-06-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200610_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(choices=[('blue_ninja.png', 'Blue Ninja 1'), ('blue_ninjax.png', 'Blue Ninja 2'), ('blue_sword_ninja.png', 'Blue Ninja w/ Swords'), ('brown_assassin.png', 'Brown Assassin'), ('cloud_ninja.png', 'Cloud Ninja'), ('dog_ninja.png', 'Dog Ninja'), ('fast_ninja.png', 'Fast Ninja'), ('fox_ninja.png', 'Fox Ninja'), ('green_ninja.png', 'Green Ninja'), ('green_samurai.png', 'Green Samurai'), ('hip_ninja.png', 'Hip Ninja'), ('kicking_ninja.png', 'Kicking Ninja'), ('knight_ninja.png', 'Knight Ninja'), ('lady_ninja.png', 'Lady Ninja'), ('ninjax_swords_gaming.png', 'Ninja Gaming w/ Swords'), ('orange_assassin.png', 'Orange Assassin'), ('orange_ninjax_gaming.png', 'Orange Ninja Gaming'), ('orange_ninjax_team.png', 'Orange Ninja Team'), ('prince_ninja.png', 'Prince Ninja'), ('purple_ninja.png', 'Purple Ninja'), ('red_ninjax_gaming.png', 'Red Ninja Gaming'), ('shinobi.png', 'Shinobi'), ('silent_ninja.png', 'Silent Ninja'), ('squad_ninja.png', 'Squad Ninja'), ('stealthy_ninja.png', 'Stealthy Ninja'), ('swift_ninja.png', 'Swift Ninja')], default='fast_ninja.png', max_length=50),
        ),
    ]
