from django.shortcuts import render, redirect
from random import randint, choice
import string
from .forms import signupForm
from .models import Signup

# Create your views here.
def home(request):
    return render(request, 'home.html')


def otp_generate():
    randomstr = ""
    for i in range(1, 4):
        digits = randint(0, 7)
        alphanumeric = choice(string.ascii_letters)
        randomstr += str(digits) + alphanumeric

        return randomstr

otp = otp_generate()


def signup(request):
    if request.method  == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = signupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def all_users(request):
    users = Signup.objects.all()
    context = {'users': users}
    return render(request, 'all_users.html', context)

def delete_user(request, pk):
    user = Signup.objects.get(id=pk)
    user.delete()
    return redirect('all_users')     