from django.db import models
import random
import string
from django.contrib.auth.models import User


def create_code():
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(5)
    )


class Event(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_code = models.CharField(max_length=5, default=create_code)
    class_date = models.DateField()
    class_title = models.CharField(max_length=25)

    def __str__(self):
        return self.class_title


class AttendanceTracker(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="attendants"
    )
    attendee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="attending"
    )
    is_attending = models.BooleanField(default=False)


class Resource(models.Model):
    CATEGORIES = [
        ("Terminology", "Terminology"),
        ("Techniques", "Techniques"),
        ("Poomsae", "Poomsae"),
        ("Workouts", "Workouts"),
        ("Exercises", "Exercises"),
        ("Acrobatics", "Acrobatics"),
        ("Extras", "Extras"),
    ]

    DIFFICULTIES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    BELT_LEVELS = [
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
    category = models.CharField(choices=CATEGORIES, max_length=25)
    title = models.CharField(max_length=50)
    description = models.CharField(
        max_length=250, null=True, default="Description not available."
    )
    difficulty = models.CharField(choices=DIFFICULTIES, max_length=25, default="Easy")
    belt_level = models.CharField(choices=BELT_LEVELS, max_length=25, default="White")
    curriculum = models.BooleanField()
    video_link_id = models.IntegerField()


class NinjaItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    media = models.ImageField(upload_to="ninja_items", blank=True)
