from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    BELTS = [
        ("White", "White"),
        ("White/Yellow", "White/Yellow"),
        ("White/Black", "White/Black"),
        ("Yellow", "Yellow"),
        ("Yellow/Black", "Yellow/Black"),
        ("Orange", "Orange"),
        ("Orange/Black", "Orange/Black"),
        ("Green", "Green"),
        ("Green/Black", "Green/Black"),
        ("Purple", "Purple"),
        ("Purple/Black", "Purple/Black"),
        ("Blue", "Blue"),
        ("Blue/Black", "Blue/Black"),
        ("Brown", "Brown"),
        ("Brown/Black", "Brown/Black"),
        ("Red", "Red"),
        ("Red/Black", "Red/Black"),
        ("Candidate", "Candidate"),
        ("Black", "Black"),
    ]
    AVATARS = [
        ('blue_ninja.png', 'Blue Ninja 1'),
        ('blue_ninjax.png', 'Blue Ninja 2'),
        ('blue_sword_ninja.png', 'Blue Ninja w/ Swords'),
        ('brown_assassin.png', 'Brown Assassin'),
        ('cloud_ninja.png', 'Cloud Ninja'),
        ('dog_ninja.png', 'Dog Ninja'),
        ('fast_ninja.png', 'Fast Ninja'),
        ('fox_ninja.png', 'Fox Ninja'),
        ('green_ninja.png', 'Green Ninja'),
        ('green_samurai.png', 'Green Samurai'),
        ('hip_ninja.png', 'Hip Ninja'),
        ('kicking_ninja.png', 'Kicking Ninja'),
        ('knight_ninja.png', 'Knight Ninja'),
        ('lady_ninja.png', 'Lady Ninja'),
        ('ninjax_swords_gaming.png', 'Ninja Gaming w/ Swords'),
        ('orange_assassin.png', 'Orange Assassin'),
        ('orange_ninjax_gaming.png', 'Orange Ninja Gaming'),
        ('orange_ninjax_team.png', 'Orange Ninja Team'),
        ('prince_ninja.png', 'Prince Ninja'),
        ('purple_ninja.png', 'Purple Ninja'),
        ('red_ninjax_gaming.png', 'Red Ninja Gaming'),
        ('shinobi.png', 'Shinobi'),
        ('silent_ninja.png', 'Silent Ninja'),
        ('squad_ninja.png', 'Squad Ninja'),
        ('stealthy_ninja.png', 'Stealthy Ninja'),
        ('swift_ninja.png', 'Swift Ninja'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(choices=AVATARS, default="fast_ninja.png", max_length=50)
    belt = models.CharField(choices=BELTS, default="White", max_length=25)
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image)

    #     if img.height > 200 or img.width > 200:
    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
