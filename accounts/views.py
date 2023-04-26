from django.shortcuts import redirect, render
from django.urls import reverse
from . forms import UserForm, ProfileForm
from django.contrib.auth import authenticate,login
from . models import Profile
# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')

    else:
        form = UserForm

    contex = {
        'form' : form
    }
    return render(request, 'registration/signup.html', contex)

def profile(request):
    
    profile = Profile.objects.get(user=request.user)
    context = {
        'myObject' : profile
    }
    return render(request, 'registration/profile.html', context)

def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userForm = UserForm(request.POST, request.FILES,instance=request.user)
        profileForm = ProfileForm(request.POST, request.FILES,instance=profile)
        if userForm.is_valid and profileForm.is_valid():
            userForm.save()
            myProfileForm = profileForm.save(commit=False)
            myProfileForm.user = request.user
            myProfileForm.save()
            return redirect("/")
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)


    context = {
        'userForm': userForm,
        'profileForm': profileForm,
    }
    return render(request, 'registration/edit_profile.html', context)