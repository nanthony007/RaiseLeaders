from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from django.contrib.auth.models import User
from main_site.models import Event, AttendanceTracker
from django.contrib.auth import authenticate, login, logout

from .models import Profile

import datetime


def custom_login(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_pass = request.POST["password"]
        user = get_object_or_404(User, email=user_email)
        if user.check_password(user_pass):
            request.session["username"] = user.username
            login(request, user)
            return redirect("calendar")
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, f"Invalid password, please try again.")
            return render(request, "users/login.html")
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("calendar")

    return render(request, "users/login.html")


def custom_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, "users/logout.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        user_email = request.POST["email"]
        user_password = request.POST["password"]
        user = User.objects.create_user(
            username=user_email,
            first_name=first_name,
            last_name=last_name,
            email=user_email,
            password=user_password,
        )
        if user:
            user.save()
            login(request, user)
            messages.success(
                request,
                f"Account created for {first_name} {last_name}. Welcome to Raise Leaders Nation.",
            )
            return redirect("calendar")
        else:
            messages.warning(request, "Invalid form entry, please try again.")
            return render(request, "users/register.html")
    return render(request, "users/register.html")


@login_required
def profile(request):
    if request.method == "POST":
        if request.POST["code"]:
            code = request.POST["code"]
            event = get_object_or_404(Event, class_code=code)
            event_set = set(
                request.user.attending.distinct("event").values_list(
                    "event_id__class_title", flat=True
                )
            )
            if event.class_title in event_set:
                messages.error(
                    request,
                    f"You've already attended this event, please use another code.",
                )
                return redirect("profile")
            attend = AttendanceTracker(
                event=event,
                attendee=request.user,
                is_attending=True,
            )
            attend.save()
            messages.success(request, f"You've successfully attended class!")
            return redirect("profile")

    delta = datetime.date.today() - request.user.profile.joined
    if request.user.profile.belt.startswith(
        "Red"
    ) or request.user.profile.belt.startswith("Candidate"):
        belt_progress = "advanced"
    else:  # lower belts
        belt = request.user.profile.belt
        required_classes = 24
        if belt == "White":
            required_classes *= 1
        elif belt == "White/Yellow":
            required_classes *= 2
        elif belt == "White/Black":
            required_classes *= 3
        elif belt == "Yellow":
            required_classes *= 4
        elif belt == "Yellow/Black":
            required_classes *= 5
        elif belt == "Orange":
            required_classes *= 6
        elif belt == "Orange/Black":
            required_classes *= 7
        elif belt == "Green":
            required_classes *= 8
        elif belt == "Green/Black":
            required_classes *= 9
        elif belt == "Purple":
            required_classes *= 10
        elif belt == "Purple/Black":
            required_classes *= 11
        elif belt == "Blue":
            required_classes *= 12
        elif belt == "Blue/Black":
            required_classes *= 13
        elif belt == "Brown":
            required_classes *= 14
        elif belt == "Brown/Black":
            required_classes *= 15
        belt_progress = (
            request.user.attending.distinct("event").count() / required_classes
        ) * 100
    context = {
        "account_days": delta.days,
        "belt_progress": belt_progress,
    }
    return render(request, "users/profile.html", context)


@login_required
def profile_update(request):
    if request.method == "POST":
        posted_email = request.POST["emailInput"]
        posted_avatar = request.POST["avatarRadios"]
        if request.user.email != posted_email:
            user = get_object_or_404(User, username=request.user.username)
            user.email = posted_email
            user.save()
            messages.success(request, f"Your email has been updated!")
        if request.user.profile.avatar != posted_avatar:
            profile = get_object_or_404(Profile, user=request.user)
            profile.avatar = posted_avatar
            profile.save()
            messages.success(request, f"Your avatar has been updated!")
        return redirect("profile")
    else:  # get
        pass
    return render(request, "users/profile_update.html")
