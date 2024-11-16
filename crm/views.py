from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, UserProfile
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages

# these are all view below.
def homepage(request):
    
    return render(request, 'crm/index.html')

def register(request):

    user_form = UserRegistrationForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user data
            user = user_form.save(commit=False)
           # You should store the password as a hashed value instead of plain text. Update the register view to hash the password using Django's make_password utility.
            user.password_hash = user_form.cleaned_data['password']  # Hashing password can be added here
            user.save()

            # Save profile data
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to login or another page after registration
        else:
            user_form = UserRegistrationForm()
            profile_form = UserProfileForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def my_login(request):
    
    render(request, 'crm/login.html')

def dashboard(request):
    
    render(request, 'crm/dashboard.html')