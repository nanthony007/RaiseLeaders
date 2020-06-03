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
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='RLBW.jpg', upload_to='profile_pics')
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
