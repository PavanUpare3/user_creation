from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully acount created')
            fm = SignupForm()

    else:
        fm = SignupForm()

    return render(request, 'signup.html', {'form':fm})
