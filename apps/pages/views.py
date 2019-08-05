from django.shortcuts import render
from django.contrib.auth.fotm import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
