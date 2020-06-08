from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from main_site.models import Event, AttendanceTracker
from django.contrib.auth import authenticate, login, logout


def custom_login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_pass = request.POST['password']
        user = get_object_or_404(User, email=user_email)
        if user.check_password(user_pass):
            request.session['username'] = user.username
            login(request, user)
            return redirect('calendar')
            
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, f"Invalid login, please try again.")
            return render(request, 'users/login.html')
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.')
        return redirect('calendar')
        
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f"Account created for {first_name} {last_name}. You are now able to login.")
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        if request.POST['code']:
            code = request.POST['code']
            event = get_object_or_404(Event, class_code=code)
            attend = AttendanceTracker(
                event=event,
                attendee=request.user,
                is_attending=True,
            )
            attend.save()

        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, r'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_update.html', context)
