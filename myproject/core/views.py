from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm

def home(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("home")

    return render(request, "home.html", {"form": form})
